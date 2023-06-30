import seaborn as sns
from matplotlib import pyplot as plt


def plot_hbar_plot(data, title: str, xlabel=None, ylabel=None, figsize=(3, 12)):
    """
    Function to plot a horizontal bar plot using seaborn.

    :param ycol:
    :param xcol:
    :param data: input data to plot
    :param title: plot title
    :param xlabel: x-axis label
    :param ylabel: y-axis label
    :param figsize: plot figsize
    :return: None
    """
    sns.set_style('whitegrid')
    sns.set(font_scale=0.8)

    if not xlabel:
        xlabel = data.name
    if not ylabel:
        ylabel = ''

    ax = sns.barplot(y=data.index, x=data.values, palette='Blues_d', orient='h')
    ax.figure.set_size_inches(figsize)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    sns.despine(left=True, bottom=True)

    return ax
