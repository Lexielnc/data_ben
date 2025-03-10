import data_ben


def main():
    # Question 1
    # TODO

    # Question 2
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Technology Usage by Age",
        question_count=5,
        category_label="mrq_age",
        categories={"Baby": 1, "Toddler": 2, "Child": 3, "Teenager": 4},
        group_label="mrq_used_q2",
        groups={"Virtual reality": 1, "Video game": 2, "Mobile": 3, "Wearable device": 4, "Robot": 5},
        group_comparison_type=data_ben.GroupComparisonType.SEPARATED,
    )

    # Question 3
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Technology Usage by Pathology",
        question_count=5,
        category_label="mrq_patho",
        categories={
            "Child developmental disorders": 1,
            "Child physical disabilities": 2,
            "Child neurological disabilities": 3,
            "Other": 4,
        },
        group_label="mrq_used_q3",
        groups={"Virtual reality": 1, "Video game": 2, "Mobile": 3, "Wearable device": 4, "Robot": 5},
        group_comparison_type=data_ben.GroupComparisonType.SEPARATED,
    )

    # Question 4
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Technology Usage by Interaction of Group",
        question_count=5,
        category_label="mrq_iog",
        categories={"Individual": 1, "Group": 2, "Both": 3},
        group_label="mrq_used_q4",
        groups={"Virtual reality": 1, "Video game": 2, "Mobile": 3, "Wearable device": 4, "Robot": 5},
        group_comparison_type=data_ben.GroupComparisonType.GROUPED,
    )

    # Question 5
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Collaboration with Professionals",
        question_count=1,
        category_label="ti_collab_q5_",
        categories={"Yes": 1, "Not sure": 3},
        group_label="ti_collab_pro_q5",
        groups={
            "Physiotherapist": 1,
            "Speech therapist": 2,
            "Nutritionist": 3,
            "Special education teacher": 4,
            "Nurse": 5,
            "Specialist doctor": 6,
            "Other": 7,
        },
        group_comparison_type=data_ben.GroupComparisonType.SEPARATED,
    )

    # Question 6
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Technology Usage by Time per Session (minutes)",
        question_count=5,
        category_label="mrq_tps",
        categories={"0-10": 1, "11-20": 2, "21-30": 3, "31-40": 4, "41-50": 5, "Unknown": 6},
        group_label="mrq_used_q6",
        groups={"Virtual reality": 1, "Video game": 2, "Mobile": 3, "Wearable device": 4, "Robot": 5},
        group_comparison_type=data_ben.GroupComparisonType.GROUPED,
    )

    # Question 7.1
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Technology Usage by First Functional Skill",
        question_count=5,
        category_label="mrq_used_q7_",
        categories={"Virtual reality": 1, "Video game": 2, "Mobile": 3, "Wearable device": 4, "Robot": 5},
        group_label="mrq_hab_1",
        groups={
            "Trunk control": 1,
            "Balance": 2,
            "Mobility / Gait": 3,
            "Lower limb(s): Strength / Endurance": 4,
            "Upper limb(s): Strength / Endurance": 5,
            "Upper limb(s): Range of motion": 6,
            "Upper limb(s): Coordination": 7,
            "Motor skills": 8,
            "Cognitive": 9,
            "Sensory": 10,
            "Pain management": 11,
            "Participation / Engagement": 12,
            "Leisure activities: Active / Quiet": 13,
            "Productivity activity: Schoolwork": 14,
            "Non-use of this technology": 15,
        },
        group_comparison_type=data_ben.GroupComparisonType.GROUPED,
    )

    # Question 7.2
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Technology Usage by Second Functional Skill",
        question_count=5,
        category_label="mrq_used_q7_",
        categories={"Virtual reality": 1, "Video game": 2, "Mobile": 3, "Wearable device": 4, "Robot": 5},
        group_label="mrq_hab_2",
        groups={
            "Trunk control": 1,
            "Balance": 2,
            "Mobility / Gait": 3,
            "Lower limb(s): Strength / Endurance": 4,
            "Upper limb(s): Strength / Endurance": 5,
            "Upper limb(s): Range of motion": 6,
            "Upper limb(s): Coordination": 7,
            "Motor skills": 8,
            "Cognitive": 9,
            "Sensory": 10,
            "Pain management": 11,
            "Participation / Engagement": 12,
            "Leisure activities: Active / Quiet": 13,
            "Productivity activity: Schoolwork": 14,
            "Non-use of this technology": 15,
        },
        group_comparison_type=data_ben.GroupComparisonType.GROUPED,
    )

    # Question 8
    data_ben.bar_chart(
        file_path="../data/VersionNumbers_CSV.csv",
        title="Advice to Families about Technology",
        question_count=1,
        category_label="ti_vad_q8_",
        categories={"Yes": 1, "No": 2, "Not sure": 3},
        group_label="ti_vad_mrq_q8",
        groups={"Virtual reality": 1, "Video game": 2, "Mobile": 3, "Wearable device": 4, "Robot": 5},
        group_comparison_type=data_ben.GroupComparisonType.SEPARATED,
    )

    # Show all plots
    data_ben.show()


if __name__ == "__main__":
    main()
