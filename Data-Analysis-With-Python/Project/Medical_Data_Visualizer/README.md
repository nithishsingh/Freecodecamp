# Medical Data Visualizer


# The Art of Medical Data Visualization 🩺📊

## An Engaging Journey into Health Insights!

Welcome to a fascinating journey delving into medical examination data! 🌟 This project invites you to wield the power of matplotlib, seaborn, and pandas to unlock the secrets hidden within these data corridors. 🚀

### Explore the Diverse Dataset

Immerse yourself in a dataset where each row embodies a unique patient, while columns hold the keys to their health narrative. From body measurements 📏 to blood test results 🩸 and lifestyle choices 🚭, this dataset is a treasure trove brimming with health-related insights.

File: medical_examination.csv

| Feature | Variable Type | Variable      | Value Type |
|:-------:|:------------:|:-------------:|:----------:|
| Age | Objective Feature | age | int (days) |
| Height | Objective Feature | height | int (cm) |
| Weight | Objective Feature | weight | float (kg) |
| Gender | Objective Feature | gender | categorical code |
| Systolic blood pressure | Examination Feature | ap_hi | int |
| Diastolic blood pressure | Examination Feature | ap_lo | int |
| Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | smoke | binary |
| Alcohol intake | Subjective Feature | alco | binary |
| Physical activity | Subjective Feature | active | binary |
| Presence or absence of cardiovascular disease | Target Variable | cardio | binary |

### Uncover Health Relationships

🔍 Your task is to reveal the intricate connections between cardiac disease, body metrics, blood markers, and lifestyle preferences. Unleash your creativity and analytical prowess to craft visuals that narrate compelling health stories.

### Navigate the Tasks Ahead

📈 Create visuals akin to `examples/Figure_1.png`, encapsulating the counts of positive and negative outcomes for `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables across cardio=1 and cardio=0.

🧮 Undertake tasks in `medical_data_visualizer.py`:
- Define an `overweight` column based on Body Mass Index (BMI).
- Standardize the data by setting 0 as ideal and 1 as adverse for `cholesterol` or `gluc`.
- Shape the data into a comprehensive chart using seaborn's `catplot()`, distinguished by 'Cardio', mirroring `examples/Figure_1.png`.
- Refine the dataset by filtering out invalid segments.
- Forge a correlation matrix from the dataset and visualize it through seaborn's `heatmap()`, masking the upper triangle, akin to `examples/Figure_2.png`.

### Chart Your Course

⚙️ Use `main.py` for crafting and fine-tuning your functions. Tap into the embedded tests from `test_module.py` available in `main.py` to validate your discoveries.

### Share Your Expedition

🌐 Capture your project's URL and embark on the journey to freeCodeCamp. Share your exploratory findings with the world!

Get ready to decode the language of health insights and turn data into captivating narratives! 🏥📈
