# Covid Revenue Loss and Company Resurgence Payment Calculator

## Purpose
Numerous times I've heard friends and family with small businesses complaining about how tedious it is to calculate revenue loss during the lockdown period to apply for government-funded covid resurgence payments.
Hence, I decided to build an application that can quickly solve this problem and display all required information and more to the business owner regarding their revenue over any given time period.

## Features 
* Revenue calculation over any given period.
* Calculate previously received resurgence payments.
* Calculate rental income over a given period and from which tenant.
* Compare revenue between two different periods. This yields percentage loss/gain figures used to derive validity for applying for resurgence payments. >= 30% loss required between pre-lockdown and post-lockdown revenue.
* Ability to choose income to ignore in revenue calculations.

## How it works?
1. Reads CSV bank files of your business over a given period.
2. Outputs revenue, rent, resurgence and other income, which can be chosen at your discretion over the particular period.

## How to use
1. Download all files for the application.
2. Run the revenue_calculator.py.
3. You will be prompted to enter the name of CSV files that contain the relevant bank information for your business.
* Note CSV bank files MUST be entered as: company_name_start_period_to_end_period_year_number_weeks ie SAMPLE_COMPANY_1_to_30_November_2021_4_weeks
4. Enter as many CSV bank files as you like.
5. The application will provide detailed revenue information for all of the entered CSV files.
6. You will be prompted to choose two periods for which to compare.
7. Application will display detailed information regarding the difference in revenue and percentage loss/gain over the two chosen periods. 
