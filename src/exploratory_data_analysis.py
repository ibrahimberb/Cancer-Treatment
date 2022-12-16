from matplotlib import pyplot as plt


COLOR = {
    "main": "#1d3557",
    "secondary": "#457b9d",
}

mapping = {
    1: "Likely Loss-of-function",
    2: "Likely Gain-of-function",
    3: "Neutral",
    4: "Loss-of-function",
    5: "Likely Neutral",
    6: "Inconclusive",
    7: "Gain-of-function",
    8: "Likely Switch-of-function",
    9: "Switch-of-function",
}


def plot_class_distribution(input_data, class_names=True):
    if class_names:
        data = input_data.copy()
        ax = data["Class"].value_counts().sort_index().plot(
            kind="bar", title="Class Distribution", xlabel="Class", ylabel="Count", rot=35, width=0.7, color=COLOR["main"]
        );
        ratios = data["Class"].value_counts().sort_index().values / data.shape[0] * 100
        for i, v in enumerate(ratios):
            plt.text(i - 0.4, 33 * (v + 0.5), str(round(v, 2)) + "%")

        # set xticklabels from mapping
        ax.set_xticklabels([mapping[i] for i in data["Class"].value_counts().sort_index().index], rotation=35, ha="right")
        # ax.set_xticklabels(data["Class"].value_counts().sort_index().index, rotation=35, ha="right")
    
    else:
        data = input_data.copy()
        ax = data["Class"].value_counts().sort_index().plot(
            kind="bar", title="Class Distribution", xlabel="Class", ylabel="Count", rot=0, width=0.7, color=COLOR["main"]
        );
        ratios = data["Class"].value_counts().sort_index().values / data.shape[0] * 100
        for i, v in enumerate(ratios):
            plt.text(i - 0.4, 33 * (v + 0.5), str(round(v, 2)) + "%")

    plt.setp(ax.xaxis.get_majorticklabels(), ha='right');


def plot_gene_distribution(input_data, top_n=25):
    # make bars thicker, color #1d3557
    ax = input_data['Gene'].value_counts()[:top_n].plot(
        kind="bar", title="Gene Distribution", xlabel="Gene", ylabel="Count", rot=45, width=0.7, color=COLOR["main"]
    );
    plt.setp(ax.xaxis.get_majorticklabels(), ha='right');


def interesting_genes(input_data, genes):
    data = input_data.copy()
    data["Class"] = data["Class"].map(mapping)
    # print(data["Class"].unique())

    for gene in genes:
        # for each gene, 
        print(f"Gene: {gene}, max number of classes: {data[data['Gene'] == gene]['Class'].nunique()}")