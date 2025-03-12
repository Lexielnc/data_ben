from enum import Enum, auto

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


class GroupComparisonType(Enum):
    SEPARATED = auto()
    GROUPED = auto()


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, delimiter=";")


def single_bar_chart(
    data: pd.DataFrame,
    title: str,
    category_label: str,
    categories: dict[str, int],
):
    # Prepare bar chart
    x = np.arange(len(categories))  # x positions for each category
    width = 0.15  # Width of each bar
    _, ax = plt.subplots(figsize=(10, 6))

    # Plot each group's data with an offset
    offsets = x  # Center bars in each category
    counts = [data[category_label].eq(categories[category]).sum() for category in categories.keys()]
    bars = ax.bar(offsets, counts, width=width, label="")

    # Add count labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        if height > 0:  # Avoid placing labels on zero-height bars
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.5,
                str(int(height)),
                ha="center",
                va="bottom",
                fontsize=10,
            )

    # Formatting
    ax.set_xticks(x)
    ax.set_xticklabels(categories.keys(), rotation=10, ha="right")
    ax.set_ylabel("Count")
    ax.set_title(title)


def groups_bar_chart(
    data: pd.DataFrame,
    title: str,
    group_label: str,
    groups: dict[str, int],
):
    # Fetch data
    data_by_group = {group: 0 for group in groups.keys()}
    for group in groups.keys():
        data_by_group[group] += data[f"{group_label}___{groups[group]}"] == 1

    # Prepare bar chart
    x = np.arange(len(groups))  # x positions for each category
    width = 0.15  # Width of each bar
    _, ax = plt.subplots(figsize=(10, 6))

    # Plot each group's data with an offset
    offsets = x  # Center bars in each category
    counts = [data_by_group[group].sum() for group in groups.keys()]
    bars = ax.bar(offsets, counts, width=width, label="")

    # Add count labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        if height > 0:  # Avoid placing labels on zero-height bars
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.5,
                str(int(height)),
                ha="center",
                va="bottom",
                fontsize=10,
            )

    # Formatting
    ax.set_xticks(x)
    ax.set_xticklabels(groups.keys(), rotation=10, ha="right")
    ax.set_ylabel("Count")
    ax.set_title(title)


def bar_chart(
    data: pd.DataFrame,
    title: str,
    question_count: int,
    category_label: str,
    categories: dict[str, int],
    group_label: str,
    groups: dict[str, int],
    use_not_applicable_group: bool,
    group_comparison_type: GroupComparisonType,
):
    # Initialize data
    data_by_group = {group: {} for group in groups.keys()}
    for group in groups.keys():
        data_by_group[group] = {category: 0 for category in categories.keys()}

    # Fetch data
    has_category = {}
    for category in categories.keys():
        for i in range(question_count):
            has_category[category] = data[f"{category_label}{i+1}"] == categories[category]

            for group in groups.keys():
                if group_comparison_type == GroupComparisonType.SEPARATED:
                    data_by_group[group][category] += (
                        data[f"{group_label}_{i+1}___{groups[group]}"] == 1
                    ) & has_category[category]
                elif group_comparison_type == GroupComparisonType.GROUPED:
                    data_by_group[group][category] += (data[f"{group_label}_{i+1}"] == groups[group]) & has_category[
                        category
                    ]
                else:
                    raise ValueError(f"Unknown group comparison type: {group_comparison_type}")

    # Prepare bar chart
    x = np.arange(len(categories))  # x positions for each category
    width = 0.15  # Width of each bar
    _, ax = plt.subplots(figsize=(10, 6))

    # Add a not applicable group
    if use_not_applicable_group:
        # Calculate the total count for each category
        groups["Not applicable"] = len(groups) + 1
        data_by_group["Not applicable"] = {}
        for category in categories.keys():
            sum_category = 0
            for group in groups.keys():
                if group == "Not applicable":
                    continue
                sum_category += data_by_group[group][category]
            data_by_group["Not applicable"][category] = (sum_category == 0) & has_category[category]

    # Plot each group's data with an offset
    for i, group in enumerate(groups.keys()):
        offsets = x + (i - len(groups) / 2) * width  # Center bars in each category
        counts = [data_by_group[group][category].sum() for category in categories.keys()]
        bars = ax.bar(offsets, counts, width=width, label=group)

        # Add count labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            if height > 0:  # Avoid placing labels on zero-height bars
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    height + 0.5,
                    str(int(height)),
                    ha="center",
                    va="bottom",
                    fontsize=10,
                )

    # Formatting
    ax.set_xticks(x)
    ax.set_xticklabels(categories.keys(), rotation=10, ha="right")
    ax.legend(title="Type")
    ax.set_ylabel("Count")
    ax.set_title(title)


def show():
    plt.show()
