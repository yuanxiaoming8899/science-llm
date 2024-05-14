<div class="Box-sc-g0xbh4-0 bJMeLZ js-snippet-clipboard-copy-unpositioned" data-hpc="true"><article class="markdown-body entry-content container-lg" itemprop="text"><div class="markdown-heading" dir="auto"><h1 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">墨子：科学的大规模语言模型</font></font></h1><a id="user-content-mozi-a-scientific-large-scale-language-model" class="anchor" aria-label="永久链接：墨子：科学的大规模语言模型" href="#mozi-a-scientific-large-scale-language-model"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/ff42248868bc1387751598955e573b397851d947f13ddd7618c0ba9e66aacdf6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f64652532304c6963656e73652d4170616368655f322e302d677265656e2e737667"><img src="https://camo.githubusercontent.com/ff42248868bc1387751598955e573b397851d947f13ddd7618c0ba9e66aacdf6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f64652532304c6963656e73652d4170616368655f322e302d677265656e2e737667" alt="代码许可" data-canonical-src="https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg" style="max-width: 100%;"></a>
<a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/678a3407e10f770d3aabd82db1fa7f373bf19425839540f85325e25072bc1e4a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e382b2d626c75652e737667"><img src="https://camo.githubusercontent.com/678a3407e10f770d3aabd82db1fa7f373bf19425839540f85325e25072bc1e4a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e382b2d626c75652e737667" alt="Python 3.8+" data-canonical-src="https://img.shields.io/badge/python-3.8+-blue.svg" style="max-width: 100%;"></a></p>
<p dir="auto"><a target="_blank" rel="noopener noreferrer" href="/gmftbyGMFTBY/science-llm/blob/main/asset/%E5%A2%A8%E5%AD%90_avatar.png"><img src="/gmftbyGMFTBY/science-llm/raw/main/asset/%E5%A2%A8%E5%AD%90_avatar.png" alt="墨子" style="max-width: 100%;"></a></p>
<p dir="auto"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">北京理工大学团队：</font></font></strong> <a href="https://github.com/gmftbyGMFTBY"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">兰天</font></font></a><sup><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">*</font></font></sup><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、车天一*、池</font></font><a href="https://github.com/CZWin32768"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">泽文</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、胡旭浩、毛先灵</font></font></p>
<hr>
<span id="user-content-all_catelogue">
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">目录：</font></font></h2><a id="user-content-catalogue" class="anchor" aria-label="永久链接： 目录：" href="#catalogue"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<ul dir="auto">
<li><a href="#introduction"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">一、简介</font></font></a></li>
<li><a href="#environment"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2. 运行 Mozi Demo</font></font></a>
<ul dir="auto">
<li><a href="#install_environment"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2.1.环境安装</font></font></a></li>
<li><a href="#download_mozi_model"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2.2.准备墨子关卡</font></font></a></li>
<li><a href="#running_demo"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2.5.部署演示</font></font></a></li>
</ul>
</li>
<li><a href="#train_scidpr"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3. 训练您自己的 SciDPR 模型</font></font></a></li>
<li><a href="#train_pandagpt"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3. 训练你自己的墨子模型</font></font></a>
<ul dir="auto">
<li><a href="#data_preparation"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.1.数据准备</font></font></a></li>
<li><a href="#training_configurations"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.2.训练配置</font></font></a></li>
<li><a href="#model_training"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.3.训练墨子</font></font></a>
<ul dir="auto">
<li><a href="#scientific_pretraining"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.3.科学预训练墨子模型</font></font></a></li>
<li><a href="#paper_ground_training"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.3.监督微调墨子模型</font></font></a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#citation"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">引文</font></font></a></li>
<li><a href="#technicalreport"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">技术报告</font></font></a></li>
<li><a href="#acknowledgments"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">致谢</font></font></a></li>
</ul>
<hr>
<span id="user-content-introduction">
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">1. 简介：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h3><a id="user-content-1-introduction-back-to-top" class="anchor" aria-label="永久链接： 1. 简介：[返回顶部]" href="#1-introduction-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Mozi是第一个针对科学论文领域的大规模语言模型，例如问答和情感支持。借助大规模语言和证据检索模型SciDPR，墨子对用户对特定论文的问题进行简洁、准确的回答，为学术研究人员提供情感支持。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">未来我们将探索墨子更多的现实应用场景，使其成为解决各种科学任务的基础模型。</font></font></p>
<hr>
<span id="user-content-environment">
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2. 运行墨子模型：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h3><a id="user-content-2-running-mozi-models-back-to-top" class="anchor" aria-label="永久链接：2. 运行 Mozi 模型：[返回顶部]" href="#2-running-mozi-models-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<span id="user-content-install_environment">
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2.1.环境安装：</font></font></h4><a id="user-content-21-environment-installation" class="anchor" aria-label="永久链接：2.1。环境安装：" href="#21-environment-installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">要安装所需的环境，请运行</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>pip install -r requirements.txt
</code></pre><div class="zeroclipboard-container">
  
    </clipboard-copy>
  </div></div>
<span id="user-content-download_mozi_model">
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2.2.准备墨子关卡：</font></font></h4><a id="user-content-22-prepare-mozi-checkpoint" class="anchor" aria-label="永久链接：2.2。准备墨子关卡：" href="#22-prepare-mozi-checkpoint"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Mozi 模型权重（在科学语料库上预训练）由预训练的大规模语言和 LoRA 权重组成。</font></font></p>
<ol dir="auto">
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">首先，请下载</font></font><a href="https://huggingface.co/decapoda-research/llama-7b-hf" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">LLaMA-7B 检查点</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">和</font></font><a href="https://huggingface.co/baichuan-inc/baichuan-7B" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Baichuan-7B 检查点</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">然后，请从以下位置下载这两个模型的 LoRA 权重：</font></font></p>
<table>
<thead>
<tr>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">LoRA 检查点</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Huggingface Delta 权重地址</font></font></th>
</tr>
</thead>
<tbody>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">百川七号B三角洲重量</font></font></td>
<td><a href="https://huggingface.co/DataHammer/mozi_baichuan_7b" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">mozi_baichuan_7b</font></font></a></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">LLaMA-7B 三角洲重量</font></font></td>
<td><a href="https://huggingface.co/DataHammer/mozi_llama_7b" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">mozi_llama_7b</font></font></a></td>
</tr>
</tbody>
</table>
</li>
<li>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">我们还发布了用于科学情感对话的 delta LoRA 模型权重，可以在</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">此处</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">找到。情感对话增量权重建立在百川七号模型的基础上。未来，我们将直接将此科学情感对话指令调优数据集与其他指令数据集（例如纸质问答和科学信息检索）进行优化。</font></font></p>
</li>
</ol>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">现在，模型参数已准备就绪。</font></font></p>
<span id="user-content-running_demo">
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2.3.部署演示：</font></font></h4><a id="user-content-23-deploying-demo" class="anchor" aria-label="永久链接：2.3。部署演示：" href="#23-deploying-demo"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">完成前面的步骤后，您可以在本地运行演示：</font></font></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>./scripts/deploy.sh

<span class="pl-c"><span class="pl-c">#</span> #!/bin/bash</span>
<span class="pl-c"><span class="pl-c">#</span> CUDA_VISIBLE_DEVICES=0 python deploy.py \</span>
<span class="pl-c"><span class="pl-c">#</span>     --model scillm-sft\</span>
<span class="pl-c"><span class="pl-c">#</span>     --model_path baichuan-inc/baichuan-7B\</span>
<span class="pl-c"><span class="pl-c">#</span>     --delta_model_path ../ckpt/scillm-emotional-sft/18\</span>
<span class="pl-c"><span class="pl-c">#</span>     --port 23333</span></pre><div class="zeroclipboard-container">
  
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">该脚本在端口上运行 Mozi 模型情感模型</font></font><code>23333</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，输入</font></font><code>POST</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请求应如下所示：</font></font></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
    <span class="pl-ent">"decoding_method"</span>: <span class="pl-s"><span class="pl-pds">"</span>greedy<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"top_p"</span>: <span class="pl-c1">0.7</span>,
    <span class="pl-ent">"top_k"</span>: <span class="pl-c1">10</span>,
    <span class="pl-ent">"penalty_alpha"</span>: <span class="pl-c1">0.5</span>,
    <span class="pl-ent">"max_new_tokens"</span>: <span class="pl-c1">128</span>,
    <span class="pl-ent">"history"</span>: [
        <span class="pl-s"><span class="pl-pds">"</span>Human: 最近科研压力真的好大啊<span class="pl-pds">"</span></span>
    ]
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
    &quot;decoding_method&quot;: &quot;greedy&quot;,
    &quot;top_p&quot;: 0.7,
    &quot;top_k&quot;: 10,
    &quot;penalty_alpha&quot;: 0.5,
    &quot;max_new_tokens&quot;: 128,
    &quot;history&quot;: [
        &quot;Human: 最近科研压力真的好大啊&quot;
    ]
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您想测试纸地对话模型，请将 替换</font></font><code>--delta_model_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为您下载的相应模型检查点权重。对于纸地对话框，输入</font></font><code>POST</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请求应如下所示：</font></font></p>
<div class="highlight highlight-source-json notranslate position-relative overflow-auto" dir="auto"><pre>{
    <span class="pl-ent">"decoding_method"</span>: <span class="pl-s"><span class="pl-pds">"</span>greedy<span class="pl-pds">"</span></span>,
    <span class="pl-ent">"top_p"</span>: <span class="pl-c1">0.7</span>,
    <span class="pl-ent">"top_k"</span>: <span class="pl-c1">10</span>,
    <span class="pl-ent">"penalty_alpha"</span>: <span class="pl-c1">0.5</span>,
    <span class="pl-ent">"max_new_tokens"</span>: <span class="pl-c1">128</span>,
    <span class="pl-ent">"evidences"</span>: [
        <span class="pl-s"><span class="pl-pds">"</span>During the first two decades of the 21st century, the sharing and processing of vast amounts of data has become pervasive ...<span class="pl-pds">"</span></span>,
        <span class="pl-s"><span class="pl-pds">"</span>One way of circumventing this problem is to anonymise the data by removing, ...<span class="pl-pds">"</span></span>,
        <span class="pl-s"><span class="pl-pds">"</span>Given that this paper is concerned with text documents (e.g. medical records), the involved techniques are related to Natural Language Processing (NLP) ...<span class="pl-pds">"</span></span>
    ],
    <span class="pl-ent">"question"</span>: <span class="pl-s"><span class="pl-pds">"</span>Which dataset do the author use in this paper?<span class="pl-pds">"</span></span>
}</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="{
    &quot;decoding_method&quot;: &quot;greedy&quot;,
    &quot;top_p&quot;: 0.7,
    &quot;top_k&quot;: 10,
    &quot;penalty_alpha&quot;: 0.5,
    &quot;max_new_tokens&quot;: 128,
    &quot;evidences&quot;: [
        &quot;During the first two decades of the 21st century, the sharing and processing of vast amounts of data has become pervasive ...&quot;,
        &quot;One way of circumventing this problem is to anonymise the data by removing, ...&quot;,
        &quot;Given that this paper is concerned with text documents (e.g. medical records), the involved techniques are related to Natural Language Processing (NLP) ...&quot;
    ],
    &quot;question&quot;: &quot;Which dataset do the author use in this paper?&quot;
}" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<hr>
<span id="user-content-train_scidpr">
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3.为墨子模型训练SciDPR模型：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h3><a id="user-content-3-train-scidpr-model-for-mozi-model-back-to-top" class="anchor" aria-label="固定链接： 3. 为 Mozi 模型训练 SciDPR 模型：[返回顶部]" href="#3-train-scidpr-model-for-mozi-model-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">SciDPR 为 Mozi 纸质问答模型提供证据检索组件，该组件检索用户查询的相关证据。有关 SciDPR 模型的详细信息，请参阅此</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/SciDPR/README.md"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">README.md</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">文件。</font></font></p>
<hr>
<span id="user-content-train_pandagpt">
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4. 训练你自己的墨子模型：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h3><a id="user-content-4-train-your-own-mozi-model-back-to-top" class="anchor" aria-label="永久链接：4.训练你自己的墨子模型：[返回顶部]" href="#4-train-your-own-mozi-model-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">前提条件：</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">在训练模型之前，请确保环境已正确安装，并且已下载 LLaMA-7B 和 Baichuan-7B 的检查点。</font></font></p>
<span id="user-content-data_preparation">
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4.1.数据准备：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h4><a id="user-content-41-data-preparation-back-to-top" class="anchor" aria-label="永久链接：4.1。数据准备：[返回顶部]" href="#41-data-preparation-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">声明：</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为了确保结果的可重复性，我们发布了训练数据集。该数据集只能用于研究目的。数据集的使用必须遵守原始来源的许可，即QASPER和SciMRC。当原作者要求时，这些数据集可能会被删除。</font></font></p>
<table>
<thead>
<tr>
<th align="center"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">训练任务</font></font></strong></th>
<th align="center"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">数据集地址</font></font></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">科学的预训练</font></font></td>
<td align="center"><a href="https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">红睡衣数据集</font></font></a></td>
</tr>
<tr>
<td align="center"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">纸磨数据集 QASPER</font></font></td>
<td align="center"><a href="https://allenai.org/data/qasper" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">QASPER-v0.3 数据集</font></font></a></td>
</tr>
<tr>
<td align="center"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">纸磨数据集 SciMRC</font></font></td>
<td align="center"><a href="https://huggingface.co/datasets/DataHammer/scimrc" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">SciMRC 数据集</font></font></a></td>
</tr>
<tr>
<td align="center"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">情感数据集</font></font></td>
<td align="center"><a href="https://huggingface.co/datasets/DataHammer/emotional_dialog" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">科学情感对话</font></font></a></td>
</tr>
</tbody>
</table>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">由于计算资源有限，我们仅从 Redpajama arXiv 语料库中收集 4B 代币用于第一版科学预训练，下载脚本可以在</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/scillm/data/pretrain/download_from_hf.py"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">此脚本</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">中找到。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">下载后，将下载的文件解压到</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/data"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">./data/</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">目录下，该目录应如下所示：</font></font></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre><span class="pl-c1">.</span>
├── pretrain
│&nbsp;&nbsp; ├── download_from_hf.py
│&nbsp;&nbsp; ├── <span class="pl-c1">test</span>
│&nbsp;&nbsp; │&nbsp;&nbsp; └── collect.py
│&nbsp;&nbsp; └── train
│&nbsp;&nbsp;     ├── combine_chinese_corpus.sh
│&nbsp;&nbsp;     └── split.sh
└── sft
    ├── alpaca
    │&nbsp;&nbsp; └── alpaca_data.json
    ├── combine.py
    ├── dolly
    │&nbsp;&nbsp; ├── download_from_hf.py
    │&nbsp;&nbsp; └── train.json
    ├── emotional
    │&nbsp;&nbsp; └── train.json
    ├── processed_qasper_test_set.json
    ├── processed_scimrc_test_set.json
    ├── qasper
    │&nbsp;&nbsp; ├── README-test.md
    │&nbsp;&nbsp; ├── README.md
    │&nbsp;&nbsp; ├── collect.py
    │&nbsp;&nbsp; ├── qasper-dev-v0.3.json
    │&nbsp;&nbsp; ├── qasper-test-and-evaluator-v0.3.tgz
    │&nbsp;&nbsp; ├── qasper-test-v0.3.json
    │&nbsp;&nbsp; ├── qasper-train-dev-v0.3.tgz
    │&nbsp;&nbsp; ├── qasper-train-v0.3.json
    │&nbsp;&nbsp; ├── qasper_dev_sft.json
    │&nbsp;&nbsp; ├── qasper_evaluator.py
    │&nbsp;&nbsp; ├── qasper_sft.json
    │&nbsp;&nbsp; ├── qasper_test_sft.json
    │&nbsp;&nbsp; ├── qasper_train_sft.json
    │&nbsp;&nbsp; ├── qasper_yes_no_test_sft.json
    │&nbsp;&nbsp; ├── qasper_yes_no_train_sft.json
    │&nbsp;&nbsp; └── scillm_test.json
    ├── scimrc
    │&nbsp;&nbsp; ├── collect.py
    │&nbsp;&nbsp; ├── scimrc_dev_sft.json
    │&nbsp;&nbsp; ├── scimrc_test_sft.json
    │&nbsp;&nbsp; ├── scimrc_train_sft.json
    │&nbsp;&nbsp; ├── scimrc_yes_no_test_sft.json
    │&nbsp;&nbsp; ├── scimrc_yes_no_train_sft.json
    │&nbsp;&nbsp; ├── smrc_dev.jsonl
    │&nbsp;&nbsp; ├── smrc_test.jsonl
    │&nbsp;&nbsp; └── smrc_train.jsonl
    └── train.json</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value=".
├── pretrain
│&nbsp;&nbsp; ├── download_from_hf.py
│&nbsp;&nbsp; ├── test
│&nbsp;&nbsp; │&nbsp;&nbsp; └── collect.py
│&nbsp;&nbsp; └── train
│&nbsp;&nbsp;     ├── combine_chinese_corpus.sh
│&nbsp;&nbsp;     └── split.sh
└── sft
    ├── alpaca
    │&nbsp;&nbsp; └── alpaca_data.json
    ├── combine.py
    ├── dolly
    │&nbsp;&nbsp; ├── download_from_hf.py
    │&nbsp;&nbsp; └── train.json
    ├── emotional
    │&nbsp;&nbsp; └── train.json
    ├── processed_qasper_test_set.json
    ├── processed_scimrc_test_set.json
    ├── qasper
    │&nbsp;&nbsp; ├── README-test.md
    │&nbsp;&nbsp; ├── README.md
    │&nbsp;&nbsp; ├── collect.py
    │&nbsp;&nbsp; ├── qasper-dev-v0.3.json
    │&nbsp;&nbsp; ├── qasper-test-and-evaluator-v0.3.tgz
    │&nbsp;&nbsp; ├── qasper-test-v0.3.json
    │&nbsp;&nbsp; ├── qasper-train-dev-v0.3.tgz
    │&nbsp;&nbsp; ├── qasper-train-v0.3.json
    │&nbsp;&nbsp; ├── qasper_dev_sft.json
    │&nbsp;&nbsp; ├── qasper_evaluator.py
    │&nbsp;&nbsp; ├── qasper_sft.json
    │&nbsp;&nbsp; ├── qasper_test_sft.json
    │&nbsp;&nbsp; ├── qasper_train_sft.json
    │&nbsp;&nbsp; ├── qasper_yes_no_test_sft.json
    │&nbsp;&nbsp; ├── qasper_yes_no_train_sft.json
    │&nbsp;&nbsp; └── scillm_test.json
    ├── scimrc
    │&nbsp;&nbsp; ├── collect.py
    │&nbsp;&nbsp; ├── scimrc_dev_sft.json
    │&nbsp;&nbsp; ├── scimrc_test_sft.json
    │&nbsp;&nbsp; ├── scimrc_train_sft.json
    │&nbsp;&nbsp; ├── scimrc_yes_no_test_sft.json
    │&nbsp;&nbsp; ├── scimrc_yes_no_train_sft.json
    │&nbsp;&nbsp; ├── smrc_dev.jsonl
    │&nbsp;&nbsp; ├── smrc_test.jsonl
    │&nbsp;&nbsp; └── smrc_train.jsonl
    └── train.json" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">下载这些数据集并保存到正确路径后，请参考数据</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/data/README.md"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">集准备教程</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">对这些数据集进行预处理，作为后续训练的语料库。</font></font></p>
<span id="user-content-training_configurations">
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4.2 训练配置：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h4><a id="user-content-42-training-configurations-back-to-top" class="anchor" aria-label="永久链接：4.2 训练配置：[返回顶部]" href="#42-training-configurations-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">为了正确训练模型，我们使用</font></font><a href="https://github.com/artidoro/qlora"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">QLoRA</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">和</font></font><a href="http://deepspeed.readthedocs.io/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">deepspeed</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">工具包。运行之前，请确保已下载这些必需的工具包。</font></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">训练相关配置如下：</font></font></p>
<table>
<thead>
<tr>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">楷模</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">型号名称</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">训练配置</font></font></th>
</tr>
</thead>
<tbody>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">科学预训练</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">斯西尔姆</font></font></td>
<td><a href="/gmftbyGMFTBY/science-llm/blob/main/config/scillm.json"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">scilm 列车</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">;</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/dsconfig/scillm.json"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">深速</font></font></a></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">纸磨SFT</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">scilm-sft</font></font></td>
<td><a href="/gmftbyGMFTBY/science-llm/blob/main/config/scillm-sft.json"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">scilm-sft-火车</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">；</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/dsconfig/scillm-sft.json"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">深速</font></font></a></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">纸磨SFT</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">scilm-sft</font></font></td>
<td><a href="/gmftbyGMFTBY/science-llm/blob/main/config/scillm-sft.json"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">scilm-sft-火车</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">；</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/dsconfig/scillm-sft.json"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">深速</font></font></a></td>
</tr>
</tbody>
</table>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">请参阅这些配置文件以获取更多培训详细信息。请注意，这些模型在 8 x 3090 (24G) GPU 上预训练了超过 9 天（超过 4B 令牌）。至于纸质问答 SFT，训练过程花费不到 3 小时（2000 个步骤）。</font></font></p>
<span id="user-content-model_training">
<div class="markdown-heading" dir="auto"><h4 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4.3.训练墨子模型：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h4><a id="user-content-43-training-mozi-models-back-to-top" class="anchor" aria-label="永久链接：4.3。训练墨子模型：[返回顶部]" href="#43-training-mozi-models-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<span id="user-content-scientific_pretraining">
<div class="markdown-heading" dir="auto"><h5 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4.3.1.科学预训练墨子模型：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">【返回顶部】</font></font></a></h5><a id="user-content-431-scientific-pre-training-mozi-models-back-to-top" class="anchor" aria-label="永久链接：4.3.1。科学预训练墨子模型：【返回顶部】" href="#431-scientific-pre-training-mozi-models-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">要使用 4B 令牌在科学预训练语料库上预训练 Mozi，请运行以下命令：</font></font></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>./scripts/train_pretrain.sh</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="./scripts/train_pretrain.sh" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">训练脚本的关键参数如下：</font></font></p>
<ul dir="auto">
<li><code>--model</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">： 中列出的型号名称</font></font><code>config/base.json</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></li>
<li><code>--model_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：大型语言模型、</font></font><code>baichuan-inc/baichuan-7B</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">baichuan-7B 模型和</font></font><code>decapoda-research/llama-7b-hf</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">LLaMA-7B 模型的检查点。</font></font></li>
<li><code>--train_data_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：该路径保存预训练语料。</font></font></li>
<li><code>--log_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：保存tensorboard格式的预训练日志的目录。该目录将自动创建。</font></font></li>
<li><code>--save_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：保存训练好的 QLoRA delta 权重的目录。该目录将自动创建。</font></font></li>
</ul>
<p dir="auto"><font style="vertical-align: inherit;"><a href="/gmftbyGMFTBY/science-llm/blob/main/config/base.yaml"><font style="vertical-align: inherit;">请注意，总训练步骤可以在./config/base.yaml</font></a></font><code>total_step</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">文件的参数</font><font style="vertical-align: inherit;">中设置</font><font style="vertical-align: inherit;">。仔细设置此参数以确保在训练期间使用所有标记。</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/config/base.yaml"><font style="vertical-align: inherit;"></font></a><font style="vertical-align: inherit;"></font></p>
<span id="user-content-paper_ground_training">
<div class="markdown-heading" dir="auto"><h5 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4.3.2.监督微调墨子模型：</font></font><a href="#all_catelogue"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">[返回顶部]</font></font></a></h5><a id="user-content-432-supversied-fine-tuning-mozi-models-back-to-top" class="anchor" aria-label="永久链接：4.3.2。监督微调墨子模型：[返回顶部]" href="#432-supversied-fine-tuning-mozi-models-back-to-top"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">此外，要在纸质问答语料库上进行有监督的微调墨子模型，首先请确保</font></font><code>dataset</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">设置为</font></font><code>QASPERDataset</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">，然后请运行以下命令：</font></font></p>
<div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>./scripts/train_sft.sh</pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="./scripts/train_sft.sh" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">训练脚本的关键参数如下：</font></font></p>
<ul dir="auto">
<li><code>--model</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">： 中列出的型号名称</font></font><code>config/base.json</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></li>
<li><code>--model_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：大型语言模型、</font></font><code>baichuan-inc/baichuan-7B</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">baichuan-7B 模型和</font></font><code>decapoda-research/llama-7b-hf</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">LLaMA-7B 模型的检查点。</font></font></li>
<li><code>--delta_model_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：第 3.3.1 节中的 LoRA 检查点加权预训练。 SFT 流程将继续针对纸质问答任务优化这些 LoRA 权重。</font></font></li>
<li><code>--train_data_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：该路径保存预训练语料。</font></font></li>
<li><code>--log_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：保存tensorboard格式的预训练日志的目录。该目录将自动创建。</font></font></li>
<li><code>--save_path</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">：保存训练好的 QLoRA delta 权重的目录。该目录将自动创建。</font></font></li>
</ul>
<p dir="auto"><font style="vertical-align: inherit;"><a href="/gmftbyGMFTBY/science-llm/blob/main/config/base.yaml"><font style="vertical-align: inherit;">请注意，总训练步骤可以在./config/base.yaml</font></a></font><code>total_step</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">文件的参数</font><font style="vertical-align: inherit;">中设置</font><font style="vertical-align: inherit;">。仔细设置此参数，以确保在训练期间使用所有标记（在我们的硬件设置中 2000 步就足够了）。</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/config/base.yaml"><font style="vertical-align: inherit;"></font></a><font style="vertical-align: inherit;"></font></p>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果要训练情感对话任务，只需将数据集替换为情感数据集路径的路径，并确保 in</font></font><code>dataset_name</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">也</font></font><code>config/bash.yaml</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">应设置为</font></font><code>EmotionalDataset</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></p>
<hr>
<span id="user-content-citation">
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">引用:</font></font></h3><a id="user-content-citation" class="anchor" aria-label="永久链接： 引用：" href="#citation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">如果您发现 Mozi 模型对您的研究或应用有用，请使用以下 BibTeX 进行引用：</font></font></p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>...
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="..." tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
<span id="user-content-technialreport">
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">技术报告：</font></font></h3><a id="user-content-technical-report" class="anchor" aria-label="永久链接： 技术报告：" href="#technical-report"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">您可以参考我们的技术报告了解更多详细信息，该报告保存在</font></font><a href="/gmftbyGMFTBY/science-llm/blob/main/asset/mozi_technical_report.pdf"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">此路径</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">中。</font></font></p>
<hr>
<span id="user-content-acknowledgments">
<div class="markdown-heading" dir="auto"><h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">致谢：</font></font></h3><a id="user-content-acknowledgments" class="anchor" aria-label="永久链接： 致谢：" href="#acknowledgments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>
<p dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">该存储库受益于</font></font><a href="https://github.com/yxuansu/OpenAlpaca"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">OpenAlpaca</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、</font></font><a href="https://panda-gpt.github.io/" rel="nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PandaGPT</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。感谢他们的精彩作品！</font></font></p>
</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></article></div>
