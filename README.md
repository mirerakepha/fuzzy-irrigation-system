#  Fuzzy Logic–Based Irrigation Decision System

direct link - https://fuzzy-irrigation-system-nxbxyakfwy4q6vcvmnv4g6.streamlit.app/

## Project Overview
This project implements a **fuzzy logic–based irrigation control system** designed to help farmers determine the optimal amount of water to irrigate crops. Traditional irrigation systems rely on precise threshold values, which are often unreliable because environmental factors such as **soil moisture**, **temperature**, and **humidity** are inherently imprecise.

To address this challenge, the system models these inputs as **fuzzy variables** and applies **fuzzy reasoning** to determine whether the irrigation water level should be **Low, Medium, or High**.

---

## Objectives
- Represent uncertain environmental data using fuzzy logic
- Apply fuzzy inference rules to make irrigation decisions
- Provide a user-friendly interface for farmers and agricultural stakeholders
- Demonstrate real-world application of fuzzy logic concepts

---

## System Description

### Input Variables
| Variable | Range | Linguistic Terms |
|--------|------|----------------|
| Soil Moisture | 0–100 % | Dry, Moderate, Wet |
| Temperature | 0–50 °C | Low, Medium, High |
| Humidity | 0–100 % | Low, Medium, High |

### Output Variable
| Variable | Range | Linguistic Terms |
|--------|------|----------------|
| Irrigation Level | 0–100 % | Low, Medium, High |

---

## 🔍 Fuzzy Logic Approach
1. **Fuzzification**  
   Crisp sensor values are converted into fuzzy values using triangular and trapezoidal membership functions.

2. **Fuzzy Rule Base**  
   Expert-defined rules such as:
   - IF soil moisture is *dry* AND temperature is *high* → irrigation is *high*
   - IF soil moisture is *wet* → irrigation is *low*

3. **Inference Engine**  
   Mamdani-style fuzzy inference is applied to evaluate rules.

4. **Defuzzification**  
   The final irrigation level is obtained as a crisp percentage using the centroid method.

---

## 🛠️ Technologies Used
- **Python**
- **scikit-fuzzy**
- **NumPy**
- **Streamlit**
- **Networkx**
- **JupyterLab**

---

## ▶️ Running the Project Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt

```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```