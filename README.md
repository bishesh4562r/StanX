This repository consists of necessary codes regarding a project on Graph Theory, based on the paper Wang, J., Xu, Y., Wang, Y. et al. KG4SL: knowledge graph neural network for synthetic lethality prediction in human cancers. Bioinformatics 37, i418–i425 (2021).
https://github.com/JieZheng-ShanghaiTech/KG4SL/tree/main
https://academic.oup.com/bioinformatics/article/37/Supplement_1/i418/6319703

Synthetic lethality (SL) a gene-pair relationship where simultaneous loss-of-function is
lethal but either loss alone is tolerated is a central concept in precision oncology, since
SL partners of genes inactivated in a tumor are candidate drug targets. KG4SL frames
SL prediction as link prediction over a biomedical knowledge graph (KG) using a graph
neural network (GNN), and reports strong general-purpose performance.
However, a model tuned for SL prediction in general has no guarantee of being well-
calibrated for any single disease context.

Our initial question was: can KG4SL be made
to work better for breast cancer specifically. But due to limited dataset we changed our
approach to Can KG4SL be modified to be more attentive towards BC biomarkers?. This
report documents a targeted architectural modification addressing that question and an
honest evaluation of what it did and did not achieve on our data and training budget.
