import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # ConCReTE: Health Insurance Data Procurement
    ## The Story So Far
    You are working on a team at Academy Health Insurance that is in charge of procuring data for
    predictive analytics. Specifically, you need to support an existing team that is forecasting future
    healthcare trends and is used to personalize insurance plans as well as optimize processing.

    This team has been been relying on the _2022 Patient and Claims Annual Report Data_ for its deployable models. The license for this data is now up for renewal. A new and different dataset is now available, the _2024 Comprehensive Patient Care and Insurance Claims Dataset._ The data scientists on the predictive analytics team have heard from others that this new dataset can add significant value to forecasts as it has higher spatialtemporal resolution and more coverage. They would like to incorporate the new data as soon as possible. The costs the renewed license for the old data and a new license for the _2024 Comprehensive Patient Care and Insurance Claims Dataset_ are the same.

    ### Role
    You are the Procurement Team Lead. You are responsible for:
    - Evaluating and acquiring high-quality datasets to improve the company's analytical models as
    measured by out-of-sample performance on future data.
    - Facilitating vendor reviews and ensuring all datasets comply with applicable provenance
    requirements, including metadata coverage, regulatory requirements, and transparent AI data
    usage.
    - Ensuring that procured data meets integration operational needs.
    - Ensuring data usage aligns with healthcare regulations and company policies.
    - Leveraging data insights for innovative marketing and improved customer trust.
    ### Business Objective
    You will create a recommendation for whether the new data should be procured or
    the old data renewed.
    - You must justify your choices to your bosses and be prepared to answer tough
    questions on how your choices add value to the organization.
    - Because of budget constraints you cannot procure both the new data and renew the
    previous data license.
    - In process of coming up with your recommendation you have the choice to get
    advice for data curators on your team, the legal team, data scientists within the
    predictive analytics team, and marketing.
    ### Data
    Below is the new dataset. You may show it to any, all, or none of the aforementioned teams to get their feedback before making your decision.
    """)
    return


@app.cell
def _():
    import pandas as pd

    df = pd.read_csv("insurance_data.csv")
    df
    return


@app.cell
def _():
    TEAM_ADVICE = {
        "Data Curators": "Assess metadata coverage: Best practices are to evaluate the dataset's metadata to ensure it includes essential information like the dataset title, unique metadata identifier, metadata location, and details about data origin and collection methods. This step is crucial for establishing the dataset's lineage, context, and usage restrictions, aligning with the company's data provenance standards. In particular, it is crucial that future information does not leak into forecasts thus the time it takes to collect the values — not just the time stamps — are important. The curator suggests that given the scale of the data being considered, 4 business days will be necessary to check the information.",
        "Legal Team": "Ensure regulatory compliance: Collaborate with the legal department to review the dataset for its adherence to healthcare data regulations, focusing on confidentiality classification, consent documentation, and data processing and storage geographies. The legal team confirms that they can complete the legal checks within 4 days.",
        "Data Scientists": "Operational efficiency and integration: Meet with the analytics team that assesses how well the dataset will integrate with existing systems and whether it can provide the expected enhancements to the analytical models without significant overhaul or disruption. What is the expected time and investment needed to incorporate the new data versus a renewal. The data analytics team confirms that they will be able to implement the new data into their pipeline with very little new code. They estimate they can train new and test new models within a week of receiving the data. They confirm their next deployment deadline is not for 21 business days.",
        "Marketing": "Strategic use and innovation: Explore how the dataset can be used to develop innovative marketing strategies and improve customer trust. This will involve touching base with the marketing team, which is focused on analyzing the dataset's intent and proprietary data presence to identify new opportunities for personalized customer engagement and service delivery. The marketing team suggests that avoiding false promises to customers is crucial."
    }
    return (TEAM_ADVICE,)


@app.cell
def _(mo):
    # Define buttons
    curator_btn = mo.ui.run_button(label="Data Curators")
    legal_btn = mo.ui.run_button(label="Legal Team")
    ds_btn = mo.ui.run_button(label="Data Scientists")
    marketing_btn = mo.ui.run_button(label="Marketing")

    # Display them
    mo.hstack([curator_btn, legal_btn, ds_btn, marketing_btn], justify="center", gap=1.0)
    return curator_btn, ds_btn, legal_btn, marketing_btn


@app.cell
def _(TEAM_ADVICE, curator_btn, ds_btn, legal_btn, marketing_btn, mo):
    advice_display = mo.md("_Click a team button above to view their advice..._")
    # Check which button was clicked and display output immediately
    if curator_btn.value:
        advice_display = mo.md(f"### 💡 Advice from Data Curators\n\n> {TEAM_ADVICE['Data Curators']}")

    elif legal_btn.value:
        advice_display = mo.md(f"### 💡 Advice from Legal Team\n\n> {TEAM_ADVICE['Legal Team']}")

    elif ds_btn.value:
        advice_display = mo.md(f"### 💡 Advice from Data Scientists\n\n> {TEAM_ADVICE['Data Scientists']}")

    elif marketing_btn.value:
        advice_display = mo.md(f"### 💡 Advice from Marketing\n\n> {TEAM_ADVICE['Marketing']}")

    advice_display

    return


@app.cell
def _(mo):
    mo.md("""
    ---
    ## Recommendation
    """)
    return


@app.cell
def _(mo):
    recommendation = mo.ui.radio(
        options={"Use data provenance standard to check new data, despite delay": 1, "Forgo data provenance standard check in order to expedite improved model performance from the new data": 2, "Forgo data provenance standard and recommend renewal of previous license": 3},
        label="Having conferred with members of your organization, what do you recommend?",
    )
    recommendation
    return


if __name__ == "__main__":
    app.run()
