# Data Setup

The portfolio-ready Stack Overflow Salary Analysis uses the **2018 Stack Overflow Developer Survey**.

The original 2019 Thinkful notebook loaded the survey from a local Windows path. The refreshed notebook instead looks for:

```text
data/survey_results_public.csv
```

## Source

Stack Overflow maintains the 2018 survey and its historical data in the official Developer Survey archive:

- 2018 survey results: https://survey.stackoverflow.co/2018/
- Official survey archive: https://github.com/StackExchange/Survey/tree/main/packages/archive/2018

The original public release contained the fields used by this project, including `Age`, `Employment`, `FormalEducation`, `YearsCodingProf`, `Salary`, `SalaryType`, `CurrencySymbol`, `WakeTime`, and `HoursComputer`.

## To rerun the notebook

1. Obtain the 2018 public survey response CSV from the official Stack Overflow survey archive or an official historical distribution.
2. Save the response file as `survey_results_public.csv` inside this `data/` directory.
3. Open `Projects/Machine_Learning/Supervised_Learning_Projects/StackOverflow_Salary_Analysis_Portfolio.ipynb`.
4. Run the notebook from the repository root so it can resolve the relative data path.

## Why the CSV is not committed here

The survey data are external source data rather than original portfolio code. Keeping the raw dataset outside the repository avoids unnecessarily increasing repository size and keeps the project focused on the analysis. The notebook documents the expected filename and source so the analysis can be reproduced with the original public data.
