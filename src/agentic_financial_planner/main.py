#!/usr/bin/env python
import os
import warnings
from datetime import datetime

import pandas as pd

from agentic_financial_planner.crew import FinancialPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs("output", exist_ok=True)


def read_user_info_from_excel(file_path="user_info.xlsx"):
    """
    Read user information from Excel file.

    Args:
        file_path: Path to the Excel file containing user information

    Returns:
        str: Formatted user information string
    """
    try:
        # Read the Excel file
        df = pd.read_excel(file_path, sheet_name=0)

        # Convert DataFrame to dictionary for easier access
        user_data = {}
        for _, row in df.iterrows():
            field = str(row.iloc[0]).strip()
            value = str(row.iloc[1]).strip()
            user_data[field] = value

        # Format the user info string
        user_info = (
            f"total_family_members: {user_data.get('total_family_members', 'N/A')}\n"
            f"earning_members: {user_data.get('earning_members', 'N/A')}\n"
            f"country: {user_data.get('country', 'N/A')}\n"
            f"local_currency: {user_data.get('local_currency', 'N/A')}\n"
            f"monthly_earnings: {user_data.get('monthly_earnings', 'N/A')}\n"
            f"monthly_expenses: {user_data.get('monthly_expenses', 'N/A')}\n"
            f"savings: {user_data.get('savings', 'N/A')}\n"
            f"debts: {user_data.get('debts', 'N/A')}\n"
            f"investment_preferences: {user_data.get('investment_preferences', 'N/A')}\n"
            f"insurance_details: {user_data.get('insurance_details', 'N/A')}\n"
            f"financial_goals: {user_data.get('financial_goals', 'N/A')}\n"
            f"number_of_children: {user_data.get('number_of_children', 'N/A')}\n"
            f"age_of_oldest_member: {user_data.get('age_of_oldest_member', 'N/A')}\n"
            f"age_of_youngest_member: {user_data.get('age_of_youngest_member', 'N/A')}\n"
            f"report_date: {datetime.now().strftime('%Y-%m-%d')}\n"
        )

        return user_info

    except FileNotFoundError:
        print(f"Error: Excel file '{file_path}' not found. Using default values.")
        return None
    except Exception as e:
        print(f"Error reading Excel file: {e}. Using default values.")
        return None


def run():
    """
    Run the crew.
    """
    # Try to read user info from Excel file, fallback to hardcoded values if file not found
    user_info = read_user_info_from_excel()

    if user_info is None:
        print("Using hardcoded user information.")
        # Fallback to hardcoded values if Excel file is not available
        user_info = (
            f"total_family_members: 3\n"
            f"earning_members: 2\n"
            f"country: India\n"
            f"local_currency: INR\n"
            f"monthly_earnings: 100000\n"
            f"monthly_expenses: 50000\n"
            f"savings: 50000\n"
            f"debts: 100000\n"
            f"investment_preferences: moderate risk\n"
            f"insurance_details: health_insurance=True, life_insurance=False, property_insurance=False\n"
            f"financial_goals: buy a house (1cr, 5 years); children's education (2000000, 14 years); retirement (4cr, 25 years)\n"
            f"number_of_children: 2\n"
            f"age_of_oldest_member: 34\n"
            f"age_of_youngest_member: 4\n"
            f"report_date: {datetime.now().strftime('%Y-%m-%d')}\n"
        )

    inputs = {"user_info": user_info}

    try:
        result = FinancialPlanner().financial_advisory_crew().kickoff(inputs=inputs)

        # print result
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)
        print("\n\nReport has been saved to output/financial_plan_report.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
