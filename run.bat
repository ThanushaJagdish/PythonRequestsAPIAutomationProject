echo ==============================
echo Running Pytest Test Suite
echo ==============================

pytest -s -v testcases/ --alluredir=reports/allure-results

echo ==============================
echo Generating Allure Report
echo ==============================

allure generate reports/allure-results -o reports/allure-report --clean

echo ==============================
echo Opening Allure Report
echo ==============================

allure open reports/allure-report

