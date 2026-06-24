import os
import pandas as pd

# 1. File Configuration
input_file = "Dataset for Data Analytics.xlsx"
output_file = "Cleaned_Data_Analytics_Project1.xlsx"

print("🔄 Step 1: Loading raw dataset into memory...")
try:
    df = pd.read_excel(input_file, sheet_name="Sheet1")
    print(f"✅ Dataset loaded successfully. Total Rows: {len(df)}")
except FileNotFoundError:
    print(
        f"❌ Error: Could not find '{input_file}'. Please place it in the same folder."
    )
    exit()

# 2. Address Missing/Null Values
print("\n🧹 Step 2: Addressing missing/null data fields...")
# The 'CouponCode' column contains 309 missing values. We replace them with 'None'
df["CouponCode"] = df["CouponCode"].fillna("None")
print("✅ Null spaces inside 'CouponCode' filled with 'None'.")

# 3. Clean Text Formats & Standardize
print("\n🔤 Step 3: Standardizing text formatting & stripping whitespace...")
text_columns = [
    "Product",
    "PaymentMethod",
    "OrderStatus",
    "ReferralSource",
    "CouponCode",
]
for col in text_columns:
    df[col] = df[col].astype(str).str.strip()
print("✅ Trailing spaces removed from all key categorical string variables.")

# 4. Standardize and Parse Dates
print("\n📅 Step 4: Standardizing date records...")
df["Date"] = pd.to_datetime(df["Date"])
print("✅ Dates converted and structured to standard YYYY-MM-DD formatting.")

# 5. Programmatic Verification Checks (MANDATED CRITERIA)
print("\n🛡️ Step 5: Running strict Data Integrity Checks...")

# Requirement: Prove ZERO duplicate Order IDs
duplicate_id_count = df.duplicated(subset=["OrderID"]).sum()
assert (
    duplicate_id_count == 0
), f"❌ Integrity Breach: Found {duplicate_id_count} duplicate OrderIDs!"
print(f"  ↳ Verification: Exactly {duplicate_id_count} duplicate OrderIDs exist.")

# Requirement: Prove ZERO incorrectly formatted dates
null_dates_count = df["Date"].isna().sum()
assert (
    null_dates_count == 0
), "❌ Integrity Breach: Unparseable date strings found!"
print(
    f"  ↳ Verification: Exactly {null_dates_count} unparseable or corrupted dates exist."
)

# Optional: Check for absolute row-by-row duplicates
entire_row_duplicates = df.duplicated().sum()
print(f"  ↳ Verification: Exactly {entire_row_duplicates} absolute duplicate rows exist.")

# 6. Export the Perfect Source of Truth
print("\n💾 Step 6: Exporting the cleaned data source...")
df.to_excel(output_file, index=False)
print(f"🚀 Success! Master clean data sheet created: '{output_file}'\n")
