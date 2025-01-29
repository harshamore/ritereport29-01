import streamlit as st

# --------------------------------------------------------------------
# Hidden Lists (Not displayed in the Streamlit App)
# --------------------------------------------------------------------

balance_sheet_labels = [
    # ASSETS (Non-current)
    "ASSETS (1) Non-current assets (a) Property, Plant and Equipment",
    "ASSETS (1) Non-current assets (b) Capital work-in-progress",
    "ASSETS (1) Non-current assets (c) Investment Property",
    "ASSETS (1) Non-current assets (d) Goodwill",
    "ASSETS (1) Non-current assets (e) Other Intangible assets",
    "ASSETS (1) Non-current assets (f) Intangible assets under development",
    "ASSETS (1) Non-current assets (g) Biological Assets other than bearer plants",
    "ASSETS (1) Non-current assets (h) Financial Assets (i) Investments",
    "ASSETS (1) Non-current assets (h) Financial Assets (ii) Trade receivables",
    "ASSETS (1) Non-current assets (h) Financial Assets (iii) Loans",
    "ASSETS (1) Non-current assets (i) Deferred assets (net) tax",
    "ASSETS (1) Non-current assets (j) Other noncurrent assets",

    # ASSETS (Current)
    "ASSETS (2) Current assets (a) Inventories",
    "ASSETS (2) Current assets (b) Financial Assets (i) Investments",
    "ASSETS (2) Current assets (b) Financial Assets (ii) Trade receivables",
    "ASSETS (2) Current assets (b) Financial Assets (iii) Cash and cash equivalents",
    "ASSETS (2) Current assets (b) Financial Assets (iv) Bank balances other than (iii)",
    "ASSETS (2) Current assets (b) Financial Assets (v) Loans",
    "ASSETS (2) Current assets (b) Financial Assets (vi) Others (to be specified)",
    "ASSETS (2) Current assets (c) Current Tax Assets (Net)",
    "ASSETS (2) Current assets (d) Other current assets",

    # EQUITY
    "EQUITY (a) Equity Share capital",
    "EQUITY (b) Other Equity",

    # LIABILITIES (Non-current)
    "LIABILITIES (1) Non-current liabilities (a) Financial Liabilities (i) Borrowings",
    "LIABILITIES (1) Non-current liabilities (a) Financial Liabilities (ia) Lease liabilities",
    "LIABILITIES (1) Non-current liabilities (a) Financial Liabilities (ii) Trade Payables (A) micro enterprises and small enterprises",
    "LIABILITIES (1) Non-current liabilities (a) Financial Liabilities (ii) Trade Payables (B) creditors other than micro/small enterprises",
    "LIABILITIES (1) Non-current liabilities (a) Financial Liabilities (iii) Other financial liabilities (to be specified)",
    "LIABILITIES (1) Non-current liabilities (b) Provisions",
    "LIABILITIES (1) Non-current liabilities (c) Deferred tax liabilities (Net)",
    "LIABILITIES (1) Non-current liabilities (d) Other noncurrent liabilities",

    # LIABILITIES (Current)
    "LIABILITIES (2) Current liabilities (a) Financial Liabilities (i) Borrowings",
    "LIABILITIES (2) Current liabilities (a) Financial Liabilities (ia) Lease liabilities",
    "LIABILITIES (2) Current liabilities (a) Financial Liabilities (ii) Trade Payables (A) micro enterprises/small enterprises",
    "LIABILITIES (2) Current liabilities (a) Financial Liabilities (ii) Trade Payables (B) creditors other than micro/small enterprises",
    "LIABILITIES (2) Current liabilities (a) Financial Liabilities (iii) Other financial liabilities",
    "LIABILITIES (2) Current liabilities (b) Other current liabilities",
    "LIABILITIES (2) Current liabilities (c) Provisions",
    "LIABILITIES (2) Current liabilities (d) Current Tax Liabilities (Net)"
]

profit_loss_labels = [
    "I Revenue From operations",
    "II Other Income",
    "IV EXPENSES (a) Cost of materials consumed",
    "IV EXPENSES (b) Purchases of Stock-in-Trade",
    "IV EXPENSES (c) Changes in inventories of finished goods, Stock-in-Trade, WIP",
    "IV EXPENSES (c) Employee benefits expense",
    "IV EXPENSES (d) Finance costs",
    "IV EXPENSES (e) Depreciation and amortization expenses",
    "IV EXPENSES (f) Other expenses",
    "V Profit/(loss) before exceptional items and tax (I-IV)",
    "VI Exceptional Items",
    "VII Profit/(loss) before exceptions items and tax (V-VI)",
    "VIII Tax expense (1) Current tax",
    "VIII Tax expense (2) Deferred tax",
    "XI Profit (Loss) for the period from continuing operations",
    "X Profit/(loss) from discontinued operations",
    "XI Tax expenses of discontinued operations",
    "XII Profit/(loss) from Discontinued operations (after tax)",
    "XIII Profit/(loss) for the period (IX+XII)",
    "XIV Other Comprehensive Income (A)(i) Items that will not be reclassified",
    "XIV Other Comprehensive Income (A)(ii) Income tax relating to items that will not be reclassified",
    "XIV Other Comprehensive Income (B)(i) Items that will be reclassified",
    "XIV Other Comprehensive Income (B)(ii) Income tax relating to items that will be reclassified",
    "XV Total Comprehensive Income for the period (XIII+XIV)",
    "XVI Earnings per equity share (for discontinued operation) (1) Basic (2) Diluted",
    "XVIII Earning per equity share (for discontinued continuing operation) (1) Basic (2) Diluted"
]

# --------------------------------------------------------------------
# Streamlit App
# --------------------------------------------------------------------
st.title("Chart of Account Input Form")

# 1. Input for Chart of Account Name
chart_of_account_name = st.text_input("Enter Chart of Account Name:")

# 2. Dropdown for selecting Debit or Credit
context = st.selectbox("Debit or Credit:", ["Debit", "Credit"])

# 3. Display user input (basic example)
st.write("## Your Selections:")
st.write("**Chart of Account Name:**", chart_of_account_name if chart_of_account_name else "_(Not entered)_")
st.write("**Context:**", context)
