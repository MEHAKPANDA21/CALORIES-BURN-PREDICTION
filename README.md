🔥 Project Overview: Calorie Burn Prediction Model
You developed a machine learning-based calorie prediction model using XGBRegressor, trained on a structured dataset sourced from Kaggle. The model estimates calories burned during physical activity based on physiological and activity-related inputs. The project not only features a robust backend but also integrates a clean front-end UI using HTML and CSS for usability.

📊 Dataset Details
The dataset includes 15,000 observations with the following features:
| Feature | Type | Description | 
| Gender | Categorical | Male or Female | 
| Age | Integer | Age in years | 
| Height | Float | Height in cm | 
| Weight | Float | Weight in kg | 
| Duration | Float | Activity duration in minutes | 
| Heart Rate | Float | Heart rate during exercise (BPM) | 
| Body Temperature | Float | Measured in °C during activity | 
| Calories Burned | Float | 🔺 Target variable | 



🧰 Libraries Used
- NumPy: For efficient numerical operations
- Pandas: Data loading and preprocessing
- Matplotlib & Seaborn: Exploratory data visualization
- Scikit-learn: Preprocessing, training pipeline, model evaluation
- XGBoost: For robust regression using gradient boosting
- Pickle: Saving and loading the trained model for deployment
- HTML & CSS: Designing a simple yet functional frontend

🚀 Model Training & Prediction Flow
You trained the model using XGBRegressor, chosen for its:
- Strength in modeling non-linear relationships
- Built-in regularization to avoid overfitting
- Fast computation on structured datasets with large samples
📌 Model Serialization: After training, the model was saved using pickle.dump()—making it easy to integrate into web applications or APIs.

🌐 Frontend Design
To improve accessibility for end users, you created a frontend interface using:
- HTML for layout and input forms
- CSS for styling and responsive design
Users can input their physiological metrics (age, gender, heart rate, etc.) directly into the browser and get an instant calorie burn estimate via your model running in the backend.
