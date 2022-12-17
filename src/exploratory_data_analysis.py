from matplotlib import pyplot as plt
import seaborn as sns

from logger import get_handler
import logging

handler = get_handler()

logger = logging.getLogger(__name__)
logger.handlers[:] = []
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.propagate = False


COLOR = {
    "main": "#1d3557",
    "secondary": "#457b9d",
    "highlight": "#a8dadc",
    "silver": "#d8d8d8"
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

reverse_mapping = {v: k for k, v in mapping.items()}


def plot_class_distribution(input_data, class_names=True, percentage_text=True):
    if class_names:
        data = input_data.copy()
        ax = data["Class"].value_counts().sort_index().plot(
            kind="bar", title="Class Distribution", xlabel="Class", ylabel="Count", rot=35, width=0.7, color=COLOR["main"]
        );
        ratios = data["Class"].value_counts().sort_index().values / data.shape[0] * 100
        if percentage_text:
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
        if percentage_text:
            for i, v in enumerate(ratios):
                plt.text(i - 0.4, 33 * (v + 0.5), str(round(v, 2)) + "%")

    plt.setp(ax.xaxis.get_majorticklabels(), ha='right');


def plot_gene_distribution(input_data, top_n=25):
    # make bars thicker, color #1d3557
    ax = input_data['Gene'].value_counts()[:top_n].plot(
        kind="bar", title="Gene Distribution", xlabel="Gene", ylabel="Count", rot=45, width=0.7, color=COLOR["main"]
    );
    plt.setp(ax.xaxis.get_majorticklabels(), ha='right');


def interesting_genes(input_data, genes, max_only=False):
    data = input_data.copy()
    data["Class"] = data["Class"].map(mapping)

    if max_only:
        for gene in genes:
            print(
                gene, "is observed as", 
                data[data["Gene"] == gene]["Class"].value_counts().index[0], data[data["Gene"] == gene]["Class"].value_counts().max(), 
                "times out of", data[data["Gene"] == gene]["Class"].value_counts().sum(), "observations."
            )
    
    else:
        for gene in genes:
            print(
                gene, "is observed as", 
                data[data["Gene"] == gene]["Class"].value_counts().index[0], data[data["Gene"] == gene]["Class"].value_counts().max(), 
                "times out of", data[data["Gene"] == gene]["Class"].value_counts().sum(), "observations."
            )
            print(data[data["Gene"] == gene]["Class"].value_counts())
            print("")


def plot_text_length_distribution(input_data):
    data = input_data.copy()
    data["TextLength"] = data["Text"].apply(lambda x: len(x.split()))
    # sort index
    ax = data.groupby('Class')['TextLength'].mean().sort_index().plot(
        kind="bar", title="Average Text Length Distribution", xlabel="Class", ylabel="Text Length", rot=35, width=0.7, color=COLOR["main"]
    );

    ax.set_xticklabels([f"{mapping[i]} ({i})" for i in data["Class"].value_counts().sort_index().index], rotation=35, ha="right")


    highlights = ["Inconclusive", "Likely Neutral", "Neutral"]

    for highlight in highlights:
        # print("highlight:", highlight)
        ax.patches[reverse_mapping[highlight] - 1].set_facecolor(COLOR["highlight"])

    plt.setp(ax.xaxis.get_majorticklabels(), ha='right');


def plot_text_char_length_distribution(input_data):
    data = input_data.copy()
    data["TextLength"] = data["Text"].apply(lambda x: len(x.split()))
    plt.figure(figsize=(8, 5))
    ax = sns.boxplot(x='Class', y='TextLength', data=data, palette="Set2")
    ax.set_xticklabels([f"{mapping[i]} ({i})" for i in data["Class"].value_counts().sort_index().index], rotation=35, ha="right")
    plt.xlabel('Class')
    plt.ylabel('# words')
    plt.title('Text Length Distribution')
    plt.setp(ax.xaxis.get_majorticklabels(), ha='right');

    
def plot_unique_genes_distribution(input_data):
    """
    Number of unique genes per class
    """
    data = input_data.copy()
    
    unique_gene_class_count = data.groupby('Class')['Gene'].nunique().to_dict()
    plt.figure(figsize=(8, 5))
    # sort index
    plt.bar(unique_gene_class_count.keys(), unique_gene_class_count.values(), color=COLOR["main"])
    # set xticklabels from mapping
    plt.xticks([i for i in unique_gene_class_count.keys()], [f"{mapping[i]} ({i})" for i in unique_gene_class_count.keys()], rotation=35, ha="right")
    plt.title('Number of Unique genes per Class')
    plt.xlabel('Class')
    plt.ylabel('# Unique Genes')
    plt.xticks(rotation=35, ha="right")
    

def plot_word_cloud(input_data):
    """
    Use wordcloud to visualize most frequent words.
    https://towardsdatascience.com/how-to-make-word-clouds-in-python-that-dont-suck-86518cdcb61f
    """
    from wordcloud import WordCloud

    # create subplot for 9 classes (3 by 3)
    fig, axes = plt.subplots(3, 3, figsize=(18, 10))
    # iterate over classes
    for i, c in enumerate(input_data["Class"].value_counts().sort_index().index):
        # select data for class
        data = input_data[input_data["Class"] == c].copy()
        # join all texts
        text = " ".join(data["Text"].values)
        # create wordcloud, black and white
        # wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
        wordcloud = WordCloud(
            background_color="white").generate(text)

        # plot wordcloud
        axes[i // 3, i % 3].imshow(wordcloud)
        axes[i // 3, i % 3].axis("off")
        axes[i // 3, i % 3].set_title(f"{mapping[c]} ({c})", fontsize=14)

        logger.debug(f"Class {c} plotted.")

    plt.tight_layout()   
