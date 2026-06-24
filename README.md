# DecodeLabs-Data-Analytics-Internship
DecodeLabs Data Analytics Internship - Project 1
📌 Project Overview
This project addresses the Data Cleaning & Preparation track for DecodeLabs. The primary objective is to take a raw ecommerce transactions file and engineer a verifiable "source of truth" by correcting formatting errors, handling structural gaps, and validating rows using strict automated checks.

** Tech Stack**
Language: Python 

Core Package: Pandas

File Engine Parser: OpenPyXL

🧼 Applied Logic & Cleaning Actions
Missing Data Mitigation: Handled 309 missing fields inside the CouponCode column by systematically applying a clean string placeholder ('None').

Text Standardization: Applied whitespace trimming (.str.strip()) to remove accidental trailing string spacing anomalies across categorical features.

Automated Validation: Coded explicit logical assertions verifying that the final pipeline yields exactly 0 duplicate transaction IDs and 0 misformatted date entries across all 1,200 rows.
