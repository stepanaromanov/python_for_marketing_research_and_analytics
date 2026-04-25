# Description 

I have acquired a solid foundation in Market Basket Analysis, mastering the intricacies of association rules, metrics, and pruning techniques. This knowledge has been applied to enhance the promotional and product placement strategies for a small grocery store.

Within the realm of association rules, I have delved into six essential metrics—supply, confidence, lift, conviction, leverage, and Zhang's metric—quantifying and evaluating relationships between various items. Applying these metrics, I successfully assisted both a library and an e-book seller in optimizing their offerings based on customer decisions.

The core challenge of Market Basket Analysis lies in translating extensive customer decisions into a concise set of valuable rules. I tackled this challenge by employing the Apriori algorithm and implementing strategies such as pruning and aggregation. Subsequently, I applied these methods to help a retailer in selecting an effective physical store layout and executing product cross-promotions.

I further honed my skills by understanding how visualizations guide the pruning process and summarize results, often manifesting as itemsets or rules. Three key visualizations—heatmaps, scatterplots, and parallel coordinates plots—were mastered and subsequently applied to assist a movie streaming service in optimizing its content strategy.

This comprehensive experience underscores my ability to not only grasp the theoretical aspects of Market Basket Analysis but also to apply this knowledge practically in diverse scenarios, driving effective decision-making for businesses.


# About Dataset

https://www.kaggle.com/datasets/irfanasrullah/groceries

## Context

The Groceries Market Basket Dataset, which can be found here. The dataset contains 9835 transactions by customers shopping for groceries. The data contains 169 unique items. The data is suitable to do data mining for market basket analysis which has multiple variables.

## Acknowledgement

Thanks to https://github.com/shubhamjha97/association-rule-mining-apriori
The data is under course Association rules mining using Apriori algorithm.
Course Assignment for CS F415- Data Mining @ BITS Pilani, Hyderabad Campus.
Done under the guidance of Dr. Aruna Malapati, Assistant Professor, BITS Pilani, Hyderabad Campus.

## Pre-processing

The csv file was read transaction by transaction and each transaction was saved as a list. A mapping was created from the unique items in the dataset to integers so that each item corresponded to a unique integer. The entire data was mapped to integers to reduce the storage and computational requirement. A reverse mapping was created from the integers to the item, so that the item names could be written in the final output file.