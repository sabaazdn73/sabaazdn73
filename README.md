<div align="center">

<img src="assets/hero.svg" alt="Saba Azadegan, structural engineer, with Fendi the cat" width="100%"/>

✦ [About](#about) · [AI evaluation](#ai-evaluation) · [Mini dApps](#mini-dapps) · [Mini apps](#mini-apps) · [Research](#research) · [Claude skills](#claude-skills) · [Photography](#photography) · [Toolkit](#toolkit) · [Courses](#courses) · [Contact](#contact) ✦

<img src="assets/divider.svg" alt="" width="100%"/>

<a id="about"></a>
<img src="assets/h-about.svg" alt="About" width="100%"/>

</div>

<p align="center"><img src="assets/saba.svg" alt="Saba" width="150"/></p>

I'm a structural engineer (MSc, Kharazmi University) with an MSc in Business from Católica Lisbon. In 2018 I worked on site on a reinforced concrete building: the quantity takeoff, the cost estimate and supervision of foundation and rebar work.

I have worked with AI for about a year: first on web3 projects, and since August 2026, as a freelancer in Portugal, on testing AI models on structural engineering tasks. My CV is in [cv/](cv/).

<div align="center">

<img src="assets/divider.svg" alt="" width="100%"/>

<a id="ai-evaluation"></a>
<img src="assets/h-hackathon.svg" alt="Structural Review Eval" width="100%"/>

<a href="https://www.youtube.com/watch?v=IWcEG7c-mQU"><img src="assets/hackathon-video.jpg" alt="Watch on YouTube: Structural Review Eval" width="100%"/></a>

▶️ **[Watch the walkthrough on YouTube](https://www.youtube.com/watch?v=IWcEG7c-mQU)** (under 5 minutes)

</div>

**Structural Review Eval** (November 2026, entered in the micro1 Eval Hackathon): six review packages for one parking structure in Salt Lake City, each with drawings, calculations, submittals and a junior engineer's draft review that looks finished and is wrong. Four models (Claude Haiku 5.5, Claude Sonnet 5.5, Gemini 3.8 Flash, Gemini 4 Argon) ran 42 trials, scored item by item against my answer keys by two graders from different model families (96% item agreement, kappa 0.91).

- **0 of 42 passed.** The models did the arithmetic (100% of the computation items) but used the neighbouring clause, an older code edition, or skipped checks the draft never raised.
- **The sandbox changed a score.** In Vertex AI's own code tool Gemini 4 Argon wrote no answer on the hardest task; in one local sandbox shared by all models it scored 8 of 14.
- **With the code library as look-up tools, 13 of 42 passed.** Governing-clause items rose from 0% to 73%, but one required check was still missed by every answer, and 10 trials ran out of turns while still reading.

<p align="center"><img src="assets/hackathon-library.png" alt="Key items earned by kind, without and with the code library as look-up tools: governing clause 0% to 73%, checks the draft did not raise 0% to 44%, current edition 21% to 50%" width="100%"/></p>

<div align="center">

<img src="assets/architecture.svg" alt="How the evaluation works: an expert designs the task, models attempt it, an equipped grader checks the answer, a report applies difficulty and quality gates, and a human signs off. A private library of adopted code editions serves the models and the grader." width="100%"/>

</div>

The tools behind it:

- **[expert-eval-harness](https://github.com/sabaazdn73/expert-eval-harness)**: runs expert tasks on Claude and Gemini models in one local sandbox and grades each answer item by item against an expert key. The grader recomputes numbers in a code sandbox, checks figures against the input files and reads the governing clause in the code library. It reports pass@k and pass^k and gates tasks on difficulty and quality.
- **A task pipeline dashboard**: the stages and human gates for building a task. A read-only copy, without prompts, keys or traps: [tnega.app/eval](https://www.tnega.app/eval/).
- **A code library as an MCP server**, private because the standards are licensed: search across ACI 318, ASCE 7 and FEMA and NIST guides, edition status, and an IBC adoption table.
- **[Where the Human Belongs](https://github.com/sabaazdn73/expert-eval-harness/blob/main/docs/where-the-human-belongs.md)**: which steps a person must check, such as the adopted code edition or the real site status, and which can go to AI.
- **[RC Code Town](https://www.tnega.app/town/)**: six concrete structures in 3D, the governing provisions and where AI tends to go wrong. It sits on [tnega.app](https://www.tnega.app), where I am also building an AI reviewer for structural drawings; it does not review drawings yet.
- **[A talk](https://www.youtube.com/watch?v=JYRgS2VCLQQ)** on how a task like these is designed, attempted by a model and graded.

<div align="center">

<img src="assets/divider.svg" alt="" width="100%"/>

<a id="projects"></a>
<img src="assets/h-projects.svg" alt="Projects" width="100%"/>

<a id="mini-dapps"></a>

### Mini dApps

<table>
<tr>
<td><a href="https://www.tnega.app/finance"><img src="assets/card-tnega.svg" alt="Tnega Finance: what each tokenized stock really costs to buy, per issuer and chain; MCP server with nine tools" width="100%"/></a></td>
<td><a href="https://github.com/sabaazdn73/Cross-Border-Payments-DDiB2026-OG04"><img src="assets/card-f2f.svg" alt="Cross-Border (F2F): a University of Zurich summer school team project I led, then extended; partner prize at ETHGlobal Lisbon 2026" width="100%"/></a></td>
</tr>
<tr>
<td><a href="https://github.com/sabaazdn73/TrustCycle"><img src="assets/card-trustcycle.svg" alt="TrustCycle: recommendation letters on IOTA" width="100%"/></a></td>
<td><img src="assets/card-receipts.svg" alt="Tnega receipts on Solana, in progress" width="100%"/></td>
</tr>
</table>

<a id="mini-apps"></a>

### Mini apps

<table>
<tr>
<td><a href="https://www.tnega.app/hava/"><img src="assets/card-hava.svg" alt="Hava: draw in the air with your hands through the webcam" width="100%"/></a></td>
<td><a href="https://github.com/sabaazdn73/open-structural-bim-course"><img src="assets/card-bim.svg" alt="Structural BIM course: 32 exercises on one reinforced concrete building in FreeCAD and Bonsai, with a checker that grades your IFC file" width="100%"/></a></td>
</tr>
<tr>
<td colspan="2" align="center"><a href="https://www.tnega.app/notebook/"><img src="assets/card-notebook.svg" alt="Review notebook: structural engineering fundamentals with worked examples and traps to test on AI" width="50%"/></a></td>
</tr>
</table>

</div>

Hava runs in the browser and the camera picture is never uploaded ([2-minute demo](https://www.youtube.com/watch?v=C0T4-EIfYHc)). The BIM course checker also runs in the browser at [tnega.app/bim](https://www.tnega.app/bim/).

<div align="center">

<a id="research"></a>

### Research

<table>
<tr>
<td><img src="assets/card-fddi.svg" alt="FDDI: structural damage detection applied to company finances, accepted at IFABS 2026" width="100%"/></td>
<td><a href="https://github.com/sabaazdn73/DIVG"><img src="assets/card-divg.svg" alt="DIVG: Digital Identity + Verification Graph, my MSc thesis" width="100%"/></a></td>
</tr>
</table>

</div>

Also: [structural reliability of reclaimed steel](https://github.com/sabaazdn73/reclaimed-steel-reliability), FORM in Python checked against importance sampling and Monte Carlo, and two sole-author conference abstracts under review (EG-ICE 2027, ISEC-2027) on where language models fail in structural review.

<div align="center">

<a id="claude-skills"></a>

### Claude skills

<table>
<tr>
<td><a href="https://github.com/sabaazdn73/heygen-avatar-director-skill-for-claude"><img src="assets/card-heygen.svg" alt="HeyGen Avatar Director: a Claude Agent Skill that directs HeyGen avatars beat by beat" width="100%"/></a></td>
<td><a href="https://github.com/sabaazdn73/gemini-veo-studio-skill-for-claude"><img src="assets/card-veo.svg" alt="Gemini Veo Studio: a Claude Agent Skill that makes videos with Google Veo 3.1" width="100%"/></a></td>
</tr>
</table>

<img src="assets/divider.svg" alt="" width="100%"/>

<a id="photography"></a>
<img src="assets/h-photography.svg" alt="Photography" width="100%"/>

<a href="https://www.tnega.app/photography/"><img src="assets/photography-grid.jpg" alt="Eight of my photographs: Mount Damavand from Lasem, a wooden balcony on an old house in Khansar, the Sheikh Lotfollah dome in Isfahan, the Belém Tower as the sun breaks through clouds, a light painting, a wristwatch on a glass-topped case in warm light, autumn leaves in a round mirror, and jacaranda trees in Lisbon" width="100%"/></a>

</div>

I have photographed since 2017, after about two years of study that started with the photography course at the University of Tehran: landscape, architecture and interiors, still life, product and food, and light painting. 238 photographs in 16 albums, on a Nikon D810 in Iran and on a phone in Lisbon and Cascais, are in my [portfolio](https://www.tnega.app/photography/).

<div align="center">

<a href="https://www.tnega.app/photography/#comfyui"><img src="assets/comfyui-grid.jpg" alt="Four images I made with ComfyUI from my own photographs: Damavand under trails of light, a tiled dome standing in the sea, a bridge at blue hour, and a glass ball holding a mountain valley" width="100%"/></a>

</div>

I also made 24 images with ComfyUI on my laptop, each from a blend of two of my photographs ([album](https://www.tnega.app/photography/#comfyui)), and brand images and logos with Gemini, ChatGPT and Claude ([Digital art album](https://www.tnega.app/photography/#digital)).

<div align="center">

<img src="assets/divider.svg" alt="" width="100%"/>

<a id="toolkit"></a>
<img src="assets/h-toolkit.svg" alt="Engineering toolkit" width="100%"/>

<img src="assets/stack-eng.svg" alt="ACI 318-19, ASCE 7, IBC, ETABS, SAFE, Abaqus, AutoCAD, Python, Excel, quantity takeoff, structural dynamics" width="100%"/>

<img src="assets/h-stack.svg" alt="Tech stack and chains" width="100%"/>

<img src="assets/stack.svg" alt="Solidity, Move, Rust, Anchor, TypeScript, Python, React, MCP, LiteSVM, Hedera, SUI, IOTA, Solana, BNB, Arbitrum" width="100%"/>

</div>

The languages and chains used in my web3 projects. I build with Claude Code; my own programming is basic.

<div align="center">

<img src="assets/divider.svg" alt="" width="100%"/>

<a id="courses"></a>
<img src="assets/h-learning.svg" alt="Courses" width="100%"/>

</div>

- Google Cloud Professional Agentic Architect, in progress since November 2026
- Anthropic Claude Academy: Introduction to Evals and AI Fluency, in progress
- Deep Dive into Blockchain, University of Zurich International Summer School, 2026
- Solana Fall School, 2026
- Google for Startups Immersion EMEA, powered by Antler, 2026

<div align="center">

<img src="assets/divider.svg" alt="" width="100%"/>

<a id="contact"></a>
<img src="assets/h-contact.svg" alt="Contact" width="100%"/>

<a href="https://www.tnega.app"><img src="assets/btn-site.svg" alt="tnega.app" height="58"/></a>
<a href="https://www.linkedin.com/in/saba-azadegan-2974b622a"><img src="assets/btn-linkedin.svg" alt="LinkedIn" height="58"/></a>
<a href="https://x.com/SabaAzadegan"><img src="assets/btn-x.svg" alt="X" height="58"/></a>
<a href="https://medium.com/@sabaazadegan"><img src="assets/btn-medium.svg" alt="Medium" height="58"/></a>

<img src="assets/footer.svg" alt="Thanks for stopping by." width="100%"/>

</div>
