# Patient Voice AI – Drug Reviews Analysis

## Overview
This project was developed as part of the **HCL Tech AI Hackathon** conducted at **IIT Delhi Campus**. The goal is to create an AI-powered system that analyzes drug reviews to provide actionable insights into patient experiences, including drug efficacy, side effects, and overall satisfaction. The system leverages advanced Natural Language Processing (NLP) techniques, machine learning models, and interactive dashboards to address the challenges of analyzing unstructured text data at scale.

---

## Problem Statement
Drug reviews are a valuable source of patient feedback, offering insights into drug efficacy, side effects, and overall satisfaction. However, manually analyzing large volumes of unstructured text data is time-consuming and prone to human bias. The challenge is to develop an AI-powered solution that can:

1. **Perform Sentiment Analysis**: Determine the overall sentiment (positive, negative, neutral) expressed by patients towards a specific drug.
2. **Topic Modeling**: Identify key themes and topics discussed in the reviews, such as efficacy against specific conditions, common side effects, and patient demographics.
3. **Predict Side Effects**: Predict potential side effects based on the review text, even if not explicitly mentioned.
4. **Provide Deeper Insights**: Extract valuable information on drug efficacy, side effects, and patient satisfaction beyond traditional clinical trial data.
5. **Improve Drug Safety and Efficacy**: Proactively identify potential safety signals, emerging side effects, and areas for drug improvement.
6. **Enhance Patient Care**: Empower patients with personalized information and support, enabling them to make informed decisions about their medication choices.

---

## Solution
The proposed solution is a comprehensive AI-powered system that includes the following components:

### 1. **Data Engineering and Manipulation**
- Built a data pipeline to load data into a database (SQLite or MySQL).
- Developed ETL (Extract, Transform, Load) jobs for data extraction and loading.

### 2. **Data Understanding and Preprocessing**
- Examined the provided datasets to understand their structure.
- Performed data cleaning and preprocessing, including handling missing values and outliers.
- Conducted exploratory data analysis (EDA) to gain insights and maximize data utility.

### 3. **Sentiment and Topic Analysis**
- Built sentiment analysis models using NLP techniques to classify reviews as positive, negative, or neutral.
- Applied topic modeling (e.g., Latent Dirichlet Allocation) to identify key themes in the reviews.
- Developed interactive dashboards to visualize trends in sentiment, topic distribution, and emerging side effect reports.

### 4. **Side Effect Prediction and Risk Assessment**
- Trained machine learning models (e.g., RNNs, Transformers) to predict potential side effects based on review text.
- Incorporated contextual information from Gen AI-generated summaries and topic analysis.

### 5. **Personalized Insights and Chatbot Interaction**
- Developed a user-friendly chatbot to answer patient queries about specific drugs, side effects, and general drug-related information.
- Provided personalized responses based on user inputs and analyzed data.

### 6. **System Integration and Deployment**
- Designed a cohesive system architecture to integrate all components.
- Proposed a deployment strategy (e.g., cloud-based, on-premises) for real-time data processing and model updates.
- Addressed scalability challenges to ensure the system can handle large volumes of data.

### 7. **Ethical Considerations and Privacy**
- Implemented measures to ensure customer privacy and data protection.
- Ensured responsible and ethical use of AI in healthcare, addressing potential biases and ensuring fairness and transparency.

---

## Dataset
The project uses the following dataset:
- **Updated_DrugReview.csv**: Contains drug reviews with information on drug name, condition, review text, rating, and side effects.

---

## Deliverables
1. **Jupyter Notebooks/Python Code**:
   - Contains the entire workflow, from data loading to model evaluation, with clear comments and explanations.

2. **Comprehensive Report**:
   - Detailed approach to the problem.
   - Data preprocessing and feature engineering techniques.
   - Model architectures and training procedures.
   - Evaluation results and model comparisons.
   - Interpretation of results and key insights.
   - Risk segmentation strategy.
   - Deployment and monitoring plan.
   - Ethical considerations and proposed guidelines.
   - Challenges faced and how they were overcome.
   - Potential improvements and future work.

3. **Python Scripts**:
   - Includes data preprocessing, model training, and evaluation scripts.

4. **Presentation**:
   - A 10-slide presentation summarizing the approach, key findings, and recommendations for non-technical stakeholders.

5. **Requirements.txt**:
   - Lists all necessary libraries and their versions.

---

## System Architecture
The system architecture consists of the following components:
1. **Data Pipeline**: ETL jobs to load and preprocess data.
2. **NLP Models**: Sentiment analysis, topic modeling, and side effect prediction.
3. **Interactive Dashboard**: Visualizes trends in sentiment, topics, and side effects.
4. **Chatbot**: Provides personalized responses to user queries.
5. **Deployment**: Cloud-based or on-premises deployment for real-time processing.

---

## How to Use
1. **Clone the Repository**:
   

2. **Set Up the Environment**:
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Flask Server**:
   - Navigate to the `server/` folder and run:
     ```bash
     python chatbot_server.py
     ```

4. **Run the Dash App**:
   - Navigate to the `app/` folder and run:
     ```bash
     python app.py
     ```

5. **Access the Dashboard**:
   - Open your browser and go to `http://127.0.0.1:8050`.

---




## Challenges and Future Work
- **Challenges**:
  - Handling unstructured and noisy text data.
  - Ensuring real-time processing and scalability.
  - Addressing ethical and regulatory concerns in healthcare AI.

- **Future Work**:
  - Incorporate more advanced NLP techniques (e.g., BERT, GPT).
  - Expand the dataset to include more drugs and conditions.
  - Integrate real-time feedback from healthcare professionals.

---


## Acknowledgments
- **HCL Tech** for organizing the AI Hackathon.
- **IIT Delhi** for hosting the event.
- The open-source community for providing valuable tools and libraries.

---

## Contact
For questions or feedback, please contact:
- [Your Email]
- [Your GitHub Profile]

---

################################## Best Wishes ########################################
```

---

### **Key Features of the README.md**
1. **Clear Structure**: Organized into sections for easy navigation.
2. **Detailed Explanation**: Explains the problem, solution, and deliverables in simple terms.
3. **Technical Details**: Includes system architecture, dataset information, and evaluation criteria.
4. **Ethical Considerations**: Highlights the importance of data privacy and bias mitigation.
5. **Future Work**: Suggests improvements and extensions for the project.

Let me know if you need further adjustments! 🚀
