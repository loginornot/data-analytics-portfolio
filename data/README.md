# Data Setup

The portfolio-ready Stack Overflow Salary Analysis uses the **2018 Stack Overflow Developer Survey**.

The original 2019 Thinkful notebook loaded the survey from a local Windows path. The refreshed notebook instead looks for:

```text
data/survey_results_public.csv
```

It also supports running the notebook from its own project folder by resolving the repository-level data directory.

## Source

Stack Overflow maintains the 2018 survey and its historical data in the official Developer Survey archive:

- 2018 survey results: https://survey.stackoverflow.co/2018/
- Official survey archive: https://github.com/StackExchange/Survey/tree/main/packages/archive/2018

The public 2018 release contains **98,855 qualified responses**. The refreshed notebook checks this row count before continuing so an incorrect survey file is not used accidentally.

The project uses fields including `Age`, `Gender`, `Employment`, `FormalEducation`, `YearsCodingProf`, `Salary`, `SalaryType`, `CurrencySymbol`, `WakeTime`, and `HoursComputer`.

## Important methodology note

The original coursework annualized monthly salary by multiplying by 12 and weekly salary by multiplying by **52**. Stack Overflow's published 2018 methodology used **50 working weeks** when creating its own annualized salary figures. The portfolio notebook intentionally preserves the original 52-week coursework logic and documents the difference.

The original notebook also filtered annualized salary to values **above $50,000 and below $195,000**.

## To rerun the notebook

1. Obtain the 2018 public survey response CSV from the official Stack Overflow survey archive or an official historical distribution.
2. Save the response file as `survey_results_public.csv` inside this `data/` directory.
3. Open `Projects/Machine_Learning/Supervised_Learning_Projects/StackOverflow_Salary_Analysis_Portfolio.ipynb`.
4. Run the notebook from the repository root or from the notebook's project directory.

## Why the CSV is not committed here

The survey data are external source data rather than original portfolio code. Keeping the raw dataset outside the repository avoids unnecessarily increasing repository size and keeps the project focused on the analysis. The notebook documents the expected filename, source, and validation checks so the analysis can be reproduced with the original public data.