import pandas as pd
import numpy as np

df = pd.read_csv('smalldedf.csv', index_col=0)

samples = pd.read_csv('https://docs.google.com/spreadsheets/d/' + 
                   '1_NePfzEcTq2VS9U1y5tpWm9tf2N6oTmEgoAjuT-YVZw' +
                   '/export?gid=0&format=csv',
                   index_col=0,
                  )



de['gene_name']=de.index.map(ensembl_genes['gene_name'])
de['gene_description']=de.index.map(ensembl_genes['gene_description'])
de['gene_id']=de.index
# de['gene_name']=de.index.map(adata.var.gene_name).astype(str)
de['gene_color'] = 'rgba(0, 50, 250, 0.5)'
de['gene_description_html'] = de['gene_description'].str.replace('\. ', '.<br>')
# de                  
              
              
jitterpval= de["pval"]+ np.random.uniform(low=-1,high=1,size=len(de["pval"]))*de["pval"].pow(4).values/625
fig = go.Figure(
    data=go.Scatter(
        x=de["lfc_mean"].round(3)
        , y=jitterpval
#         , y=de["pval"].round(3)
        , mode='markers'
        , marker=dict(color=de['gene_color'])
        , hoverinfo='text'
        , text=de['gene_description_html']
        , customdata=de.gene_name.astype(str) + '<br>' + de.gene_id.values + \
                     '<br>-log10(p-value): \t' + de["pval"].round(3).astype(str) + \
                     '<br>log2 FC mean: \t' + de["lfc_mean"].round(3).astype(str) + \
                     '<br>log2 FC std: \t' + de["lfc_std"].round(3).astype(str)
        , hovertemplate='%{customdata} <br><extra>%{text}</extra>'
    )
    , layout={
        "title": {"text":
                      "Differential expression on "+ str(group1) + ' vs ' + str(group2)
            , 'x': 0.5
                  }
        , 'xaxis': {'title': {"text": "log fold change"}}
        , 'yaxis': {'title': {"text": "-log10(p-value)"}}
        , 'width':1200
        , 'height': 800
    }
)

fig.update_layout(hovermode='closest')
fig.add_shape(type="line", x0=-10, y0=3, x1=10, y1=3,
             line=dict(color="Red",width=2,dash="dash",) 
             )
fig.update_layout(
    hoverlabel=dict(
#         bgcolor="white",
#         font_size=16,
#         font_family="Rockwell"
    )
)
fig.update_layout(template='none')
fig.show()              
