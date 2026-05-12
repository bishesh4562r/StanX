# Synthetic Lethality Prediction in Breast Cancer using Graph Neural Networks
## Papers & Resources with Links

---

# Foundational SL & GNN Methods

## 1. KG4SL (Wang et al., 2021 — Bioinformatics)
**Title:** *KG4SL: knowledge graph neural network for synthetic lethality prediction in human cancers*

- Oxford Academic:  
  [KG4SL Paper](https://academic.oup.com/bioinformatics/article/37/Supplement_1/i418/6319703?utm_source=chatgpt.com)
- PDF mirror:  
  [KG4SL PDF](https://www.researchgate.net/publication/353207979_KG4SL_Knowledge_graph_neural_network_for_synthetic_lethality_prediction_in_human_cancers?utm_source=chatgpt.com)

---

## 2. SLGNN (Zhu et al., 2023 — Bioinformatics)
**Title:** *SLGNN: synthetic lethality prediction in human cancers based on factor-aware knowledge graph neural network*

- Oxford Academic:  
  [SLGNN Paper](https://academic.oup.com/bioinformatics/article/39/2/btad015/6988048?utm_source=chatgpt.com)
- PDF mirror:  
  [SLGNN PDF](https://www.researchgate.net/publication/367187421_SLGNN_Synthetic_lethality_prediction_in_human_cancers_based_on_factor-aware_knowledge_graph_neural_network?utm_source=chatgpt.com)

---

## 3. DGIB4SL (2025 — Briefings in Bioinformatics)
**Title:** *Interpretable High-order Knowledge Graph Neural Network for Predicting Synthetic Lethality in Human Cancers*

- arXiv:  
  [DGIB4SL arXiv](https://arxiv.org/abs/2503.06052?utm_source=chatgpt.com)

---

## 4. MVGCN-iSL (Frontiers in Genetics, 2023)
**Title:** *MVGCN-iSL: multi-view graph convolutional networks for cell-specific synthetic lethality prediction*

- Frontiers:  
  [MVGCN-iSL Paper](https://www.frontiersin.org/journals/genetics?utm_source=chatgpt.com)

---

# Benchmarking Paper

## Nature Communications (2025)
**Topic:** Benchmarking ML methods for synthetic lethality prediction

- Nature Communications:  
  [Nature Benchmark Paper](https://www.nature.com/ncomms/?utm_source=chatgpt.com)

---

# Biology Background

## BRCA1 / BRCA2 & Synthetic Lethality
- PubMed Central:  
  [BRCA Synthetic Lethality Review](https://pmc.ncbi.nlm.nih.gov/?utm_source=chatgpt.com)

---

## PARP Inhibitors & Resistance Mechanisms
- Wiley Online Library:  
  [PARPi Resistance Review](https://onlinelibrary.wiley.com/?utm_source=chatgpt.com)

---

# Databases & Resources

## SynLethDB 2.0
- [SynLethDB 2.0](https://synlethdb.sist.shanghaitech.edu.cn/?utm_source=chatgpt.com)

## DepMap
- [DepMap](https://depmap.org/portal/?utm_source=chatgpt.com)

## CCLE
- [CCLE](https://sites.broadinstitute.org/ccle/?utm_source=chatgpt.com)

## TCGA BRCA
- [TCGA Data Portal](https://portal.gdc.cancer.gov/?utm_source=chatgpt.com)

## STRING
- [STRING Database](https://string-db.org/?utm_source=chatgpt.com)

## BioGRID
- [BioGRID](https://thebiogrid.org/?utm_source=chatgpt.com)

## IntAct
- [IntAct](https://www.ebi.ac.uk/intact/?utm_source=chatgpt.com)

## KEGG
- [KEGG](https://www.genome.jp/kegg/?utm_source=chatgpt.com)

## Reactome
- [Reactome](https://reactome.org/?utm_source=chatgpt.com)

## Gene Ontology
- [Gene Ontology](https://geneontology.org/?utm_source=chatgpt.com)

## DrugBank
- [DrugBank](https://go.drugbank.com/?utm_source=chatgpt.com)

## ChEMBL
- [ChEMBL](https://www.ebi.ac.uk/chembl/?utm_source=chatgpt.com)

## SL-Miner
- [SL-Miner](https://github.com/?utm_source=chatgpt.com)

---

# GNN Frameworks

## PyTorch Geometric
- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/?utm_source=chatgpt.com)

## DGL
- [Deep Graph Library (DGL)](https://www.dgl.ai/?utm_source=chatgpt.com)

---

# Explainability Tools

## GNNExplainer
- [GNNExplainer Paper](https://arxiv.org/abs/1903.03894?utm_source=chatgpt.com)

## SubgraphX
- [SubgraphX Paper](https://arxiv.org/abs/2102.05152?utm_source=chatgpt.com)

---

# Databases & Tools

| Category | Resource | What you get | Link |
|---|---|---|---|
| SL labels | SynLethDB 2.0 | Curated + experimental SL pairs, breast cancer query | https://synlethdb.sist.shanghaitech.edu.cn |
| Functional genomics | DepMap (Chronos scores) | CRISPR knockout viability across cell lines | https://depmap.org/portal |
| Cell line omics | CCLE | Gene expression, mutation, copy number | https://sites.broadinstitute.org/ccle |
| Patient genomics | TCGA BRCA | Tumor mutation profiles, survival data | https://portal.gdc.cancer.gov |
| PPI | STRING | Protein interaction edges | https://string-db.org |
| PPI | BioGRID | Protein interaction edges | https://thebiogrid.org |
| PPI | IntAct | Protein interaction edges | https://www.ebi.ac.uk/intact |
| Pathways | KEGG | Pathway co-membership edges | https://www.genome.jp/kegg |
| Pathways | Reactome | Pathway co-membership edges | https://reactome.org |
| Pathways | Gene Ontology (GO) | Functional and pathway annotations | https://geneontology.org |
| Drug targets | DrugBank | Link SL partners to drugs | https://go.drugbank.com |
| Drug targets | ChEMBL | Drug-target bioactivity data | https://www.ebi.ac.uk/chembl |
| Evidence mining | SL-Miner | Statistical SL evidence from multi-omics | https://github.com |
| GNN framework | PyTorch Geometric | GCN, GAT, RGCN, HeteroConv | https://pytorch-geometric.readthedocs.io |
| Graph analysis | NetworkX | Graph preprocessing and analysis | https://networkx.org |
| Graph analysis | DGL | Graph preprocessing, motif counting | https://www.dgl.ai |
| Explainability | GNNExplainer | Subgraph extraction for predictions | https://arxiv.org/abs/1903.03894 |
| Explainability | SubgraphX | Explainable subgraph discovery | https://arxiv.org/abs/2102.05152 |

