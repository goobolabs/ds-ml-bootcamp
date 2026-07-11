# 1. What did I build?

I built a machine learning pipeline to group (or "segment") wholesale customers based on how they spend their money over the year. I focused only on six spending categories, like Fresh food, Milk, and Grocery. I purposely left out background info like "Region" or "Channel" because I wanted the algorithms to group people based strictly on their shopping habits.

To stop a few massive buyers from messing up the results, I used a math trick called an IQR cap (set to 1.5) to gently rein in those extreme values.

I also created a visual chart called the "Elbow Curve" using matplotlib. Looking at how the error dropped on the chart helped me decide that 3 clusters (k=3) was the best number of groups to use.

To see how different methods handle the data, I tried two different approaches:

First, I used a StandardScaler (which centers the data) and fed it into a K-Means clustering model.

Second, I used a MinMaxScaler (which squishes all the numbers between 0 and 1) and fed it into an Agglomerative (Hierarchical) Clustering model to compare the results.

# 2. What do these customer groups mean?

By looking at the center points (centroids) of the K-Means clusters and converting the numbers back to real dollars, we can easily see who these customers are. Since I used 3 clusters, here is what two of the most distinct groups look like:

The Fresh Food Buyers (Restaurants & Cafes): This group spends a lot of money on Fresh products but very little on things like Detergents_Paper or canned Grocery items. These are almost certainly restaurants, cafes, or delis that need fresh ingredients daily.

Business Action: We should offer these customers a "Daily Fresh" subscription. If we give them early-morning, fast deliveries, they will stay loyal to us because fresh food is the lifeblood of their business.

The Supermarket Shoppers (Retailers): This group spends massive amounts on Grocery, Milk, and Detergents_Paper. These are large grocery stores or convenience shops that buy non-perishable goods and cleaning supplies to put on their shelves.

Business Action: We should offer them bulk discounts. For example, a promotion like "Buy 5 pallets of paper towels, get 10% off your milk order" would encourage them to spend more money per invoice.

# 3. How does K-Means actually work?

K-Means is an algorithm that groups data around center points called "centroids." You have to tell it how many groups you want beforehand (in my case, 3). It works in a simple, repeating loop:

Drop the pins: It randomly drops 3 center points into the data.

Group up: It looks at every customer and assigns them to whichever center point is closest to them.

Find the middle: It then looks at the new groups it just made, finds the exact middle of the group, and moves the center point there.

It just repeats steps 2 and 3 until the center points stop moving. Once they settle, the data is officially clustered!

# 4. My Second Algorithm: Agglomerative Clustering

For my second method, I used Agglomerative Clustering along with MinMaxScaler. I wanted to see how a completely different style of algorithm would react to data that was strictly boxed between 0 and 1.

Here is what I learned about it:

How it works: Instead of dropping pins from the top down, this algorithm builds from the bottom up. It starts by treating every single customer as their own tiny group. Then, it finds the two customers that are most similar and pairs them up. It keeps finding the closest groups and pairing them together until only 3 large groups are left.

The Good: It doesn't force the groups to be perfectly round like K-Means does, and it can build a cool visual tree (called a dendrogram) that shows exactly how the groups merged together.

The Bad: It requires a lot of computing power. Because it has to calculate the distance between every single customer and every other customer, it becomes incredibly slow if you have millions of rows of data.

The Results: Both K-Means and Agglomerative Clustering gave me similar "Silhouette Scores" (which measure how well-separated the groups are). This proves that both methods successfully found real, underlying patterns in how people shop, even though their logic and scaling were totally different.

# 5. Final Recommendation

For this specific project, I highly recommend using the K-Means clustering approach with StandardScaler.

While the Agglomerative method was a great experiment, K-Means is way faster, making it a better choice as our wholesale business grows and adds thousands of new customers. Most importantly, the K-Means "centroids" represent a literal "average customer" in exact dollar amounts. It is incredibly easy to hand those numbers to a sales manager and say, "This is exactly what our average Group 1 customer buys," making it much easier for humans to understand and use for real business decisions.