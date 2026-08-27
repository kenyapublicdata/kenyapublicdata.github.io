# Data Directory

The data lifecycle is `Raw → Interim → Processed → Published`.

- Never overwrite raw files.
- Every transformation should be reproducible and documented.
- Use CSV for portable tabular releases and Parquet when scale or types justify it.
- Keep data units and frequency explicit.
- The exact data underlying a released figure belongs in `Published/`.

