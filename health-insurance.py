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
def _(mo):
    # --- Configuration ---
    TEAM_ADVICE = {
        "Data Curators": "As data curators, we recommend evaluating the metadata quality...",
        "Legal Team": "From a legal perspective, verify compliance with HIPAA, GDPR...",
        "Data Scientists": "The new dataset offers higher spatiotemporal resolution...",
        "Marketing": "Incorporating this data could enable more personalized insurance plans..."
    }
    TEAMS = list(TEAM_ADVICE.keys())
    get_team, set_team = mo.state(None, allow_self_loops=True)
    return (TEAMS, TEAM_ADVICE, get_team, set_team)
    
@app.cell
def _(mo, TEAMS, get_team, set_team):
    # Create the buttons
    button_list = []
    for team in TEAMS:
        # 1. Read State (to set color)
        is_active = (get_team() == team)
        kind = "success" if is_active else "neutral"
        
        # 2. Write State (on click)
        def on_click(t=team):
            if get_team() == t:
                set_team(None)
            else:
                set_team(t)
                
        button_list.append(
            mo.ui.button(label=team, kind=kind, on_click=on_click)
        )

    # FIX 2: Wrap in mo.ui.array to ensure global tracking of the list
    button_group = mo.ui.array(button_list)

    # Display the group
    mo.hstack(button_group, justify="center", gap=1.0)
    return

@app.cell
def _(mo, get_team, TEAM_ADVICE):
    current = get_team()
    display_advice = mo.md(None)
    if not current:
        display_advice
    else:
        advice = TEAM_ADVICE.get(current, "")
        display_advice = mo.md(
            f"""
            ### 💡 Advice from {current}
            ---
            > {advice}
            """
        )
    display_advice
    return