# COVID-19 Risk Assessment Alexa Skill

Voice-based risk evaluation system using Alexa Skills Kit

## Files

### lambda_function.py
- Handles dialog flow and risk calculation
- Implements 8 core intents:
  - answerIntent: Starts assessment (trigger: "ready")
  - ageIntent: Processes numeric age input
  - genderIntent: Handles gender selection
  - bodyTempIntent: Checks fever status
  - diseaseIntent: Tracks symptoms
  - severeDiseaseIntent: Identifies critical symptoms
  - travelIntent: Verifies travel history
  - statusIntent: Final risk evaluation

### interactions.json
- Interaction model with:
  - Invocation name: "corona test"
  - 7 custom slot types:
    - gender (male/female/transgender)
    - fever (high/normal)
    - disease (coughing/sneezing/etc)
    - severeDisease (chest pressure/breathing difficulty)
    - past (medical history)
    - travel (travel history)
    - status (symptom progression)
  - Intent-slots mapping:
    | Intent              | Slot Type          | Purpose                 |
    |---------------------|--------------------|-------------------------|
    | ageIntent           | AMAZON.NUMBER      | Age input               |
    | genderIntent        | gender             | Gender selection        |
    | bodyTempIntent      | fever              | Fever status            |
    | diseaseIntent       | disease            | Symptom tracking        |
    | severeDiseaseIntent | severeDisease      | Critical symptoms       |
    | travelIntent        | travel             | Travel history          |
    | pastIntent          | past               | Medical history         |
    | statusIntent        | status             | Symptom progression     |

## Risk Calculation
- Scores (0-13+ points) based on:
  - Age: +0-3
  - Gender: +1 (male)
  - Fever: +1
  - Symptoms: +1
  - Severe symptoms: +2
  - Travel history: +2
  - Pre-existing conditions: +2
  - Symptom progression: -1 to +2

- Risk levels:
  - <5: Low risk
  - 5-10: Moderate risk
  - 10-13: High risk
  - >13: Critical risk

## Important Notes
⚠️ Not medical advice - consult professionals for health concerns  
⚠️ Uses global variable for scoring (not production-safe)  
⚠️ Sequential single-user interaction model
