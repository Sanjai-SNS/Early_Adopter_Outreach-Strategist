# 📁 early_user_outreach_app/agents/timing_suggester.py
def suggest_outreach_timing(platforms):
    timing = {}
    for platform in platforms:
        if "Reddit" in platform:
            timing[platform] = "Post between 8-10am PST for max visibility"
        elif "Twitter" in platform:
            timing[platform] = "Tweet between 11am-1pm or 5-6pm local time"
        elif "Email" in platform:
            timing[platform] = "Send on Tue-Thu at 9am or 2pm"
        else:
            timing[platform] = "Weekdays 10am-4pm local time"
    return timing
