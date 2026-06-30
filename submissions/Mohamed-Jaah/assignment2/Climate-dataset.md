# Annual Climate Condition Dataset (Rainy vs. Drought Year)

**Rows:** 50 | **Columns:** 7 (1 ID + 5 features + 1 label) | **Format:** raw, uncleaned (as collected)

**Columns:** `RecordID`, `RainfallAmount_mm`, `AvgTemperature_C`, `Humidity_percent`, `RainyDaysCount`, `SoilMoistureLevel`, `ClimateCondition`

> Note: `—` indicates a missing (blank) value as recorded in the original log. Inconsistent text (e.g., `Med`, `MEDIUM`, `low `, `drought`, `RAINY`), the comma-typo entry (`12,5`), and out-of-range/outlier values (e.g., `AvgTemperature_C = 70.0`, `RainfallAmount_mm = 999.0`, `Humidity_percent = 130`) are left untouched intentionally — this is the raw dataset prior to Lesson 3 preprocessing. Record `R007` appears twice (duplicate entry).

| RecordID | RainfallAmount_mm | AvgTemperature_C | Humidity_percent | RainyDaysCount | SoilMoistureLevel | ClimateCondition |
|---|---|---|---|---|---|---|
| R013 | 99.1 | 22.3 | 71 | 13 | Med | Rainy |
| R018 | 61.3 | 25.4 | 61 | 8 | LOW | drought |
| R040 | 30.8 | 23.8 | 61 | 5 | Medium | drought |
| R023 | 48.6 | 27.9 | 48 | 0 | High | Drought |
| R019 | 86.8 | 26.2 | 59 | 10 | Low | Drought |
| R047 | 103.2 | 22.9 | 59 | 20 | High | Rainy |
| R007 | 55.1 | 26.0 | 71 | 4 | High | Drought |
| R012 | 62.6 | 26.0 | 55 | — | high | Drought |
| R004 | 147.7 | 22.0 | 82 | 17 | High | — |
| R027 | 97.6 | 29.5 | 52 | 16 | High | Drought |
| R039 | 121.1 | 24.5 | 74 | 13 | MEDIUM | Rainy |
| R038 | 19.9 | 29.1 | 34 | 0 | Medium | Drought |
| R037 | 62.7 | 26.2 | 55 | 13 | Low | Drought |
| R008 | 101.3 | 30.3 | 53 | 5 | Medium | Drought |
| R001 | 71.3 | 27.1 | 49 | 4 | Low | Drought |
| R024 | 46.3 | 26.8 | 55 | 7 | HIGH | Drought |
| R029 | 72.3 | 23.2 | 51 | 14 | High | rainy |
| R009 | 127.7 | 23.7 | 62 | 16 | High | Rainy |
| R011 | 132.1 | 19.2 | 52 | 15 | Medium | RAINY |
| R049 | 22.6 | 32.6 | 26 | 4 | Med | drought |
| R026 | 54.1 | 25.1 | 54 | 9 | Low | Drought |
| R003 | 97.7 | 22.0 | 47 | 7 | High | Drought |
| R007 | 55.1 | 26.0 | 71 | 4 | High | Drought |
| R028 | 64.3 | 28.4 | 130 | 7 | High | Drought |
| R021 | 65.9 | 31.9 | 30 | 3 | low | Drought |
| R020 | 68.2 | 29.5 | 45 | 9 | Low | Drought |
| R002 | 60.1 | 26.9 | 53 | 10 | high | — |
| R045 | 51.3 | 33.5 | — | 6 | Medium | drought |
| R010 | 17.1 | 25.7 | 46 | 12,5 | medium | Drought |
| R022 | 106.6 | 24.8 | 79 | 11 | High | rainy |
| R036 | 32.2 | 32.1 | 35 | 6 | Med | Drought |
| R046 | 68.9 | 26.4 | 62 | 10 | medium | Drought |
| R041 | 36.0 | 24.8 | 43 | 1 | high | Drought |
| R025 | 70.5 | 30.3 | 29 | 10 | HIGH | Drought |
| R032 | 149.5 | 24.3 | 66 | 17 | High | Rainy |
| R030 | 49.1 | 24.8 | 60 | 10 | High | Drought |
| R015 | 86.3 | 26.3 | 67 | 11 | Medium | Rainy |
| R014 | 93.4 | 24.7 | 67 | 11 | High | Rainy |
| R016 | 999.0 | 25.2 | 59 | 1 | Med | Drought |
| R042 | 92.9 | 31.1 | 49 | 9 | MEDIUM | Drought |
| R044 | 30.4 | 30.6 | 64 | 9 | High | Drought |
| R017 | 19.0 | 30.1 | 36 | 7 | Medium | Drought |
| R031 | 101.0 | 20.2 | 78 | 12 | Low | Rainy |
| R005 | 113.4 | 70.0 | — | 9 | Low | Drought |
| R034 | 95.5 | 27.4 | 56 | 12 | Low | Drought |
| R043 | 99.9 | 28.3 | 68 | 12 | Low | Drought |
| R006 | 113.5 | 24.3 | — | 7 | — | Drought |
| R035 | 99.3 | 26.7 | 64 | 13 | Low | Rainy |
| R033 | 64.3 | 29.1 | 47 | 9 | Medium | drought |
| R048 | 84.5 | 25.8 | 63 | 10 | low | Drought |
