# Saba Azadegan

Structural engineer (MSc) · AI evaluation for structural engineering

Lisbon, Portugal · [sabaazad93@gmail.com](mailto:sabaazad93@gmail.com)

[linkedin.com/in/saba-azadegan-2974b622a](https://www.linkedin.com/in/saba-azadegan-2974b622a/) · [github.com/sabaazdn73](https://github.com/sabaazdn73) · [tnega.app](https://www.tnega.app) · [medium.com/@sabaazadegan](https://medium.com/@sabaazadegan)

**Visual CV with all my projects: [claude.ai/artifact/JLwnJnxrruLnH2ggXPExnt](https://claude.ai/artifact/JLwnJnxrruLnH2ggXPExnt)**

**Freelancer registered in Portugal, available now for project contracts. I can work with your team from Lisbon and travel to your office or wherever the work requires. Open to relocation if a work visa can be sponsored.**

## Profile

I am a structural engineer, and my main work is AI evaluation for structural engineering: I write expert review tasks from realistic project documents, measure how often AI models get the code checks right and report where they fail. Behind this are 18 months of graduate research on damage detection in bridges, site work on a reinforced concrete building and an MSc in Business from Católica Lisbon. I build most of my tools with Claude Code and want to help make AI reliable for work that an engineer must sign off.

## Education

### MSc in Business
*Católica Lisbon School of Business and Economics, Portugal · Sep 2023 to Oct 2026 · Final average 14/20 · Taught in English*

- Thesis (17/20), “Digital Identity + Verification Graph”: impact claims are verified once by a panel of stakeholders and can then be checked by any investor; tested in a 5,000-round simulation in Python, with a prototype live on Sui testnet ([divg.vercel.app](https://divg.vercel.app)).

### MSc in Civil Engineering, Structural Engineering
*Kharazmi University, Iran · Oct 2018 to Feb 2021 · GPA 15.75/20 (programme average 14.95/20)*

- Finite Element Methods (18/20), Theory of Elasticity (18.25/20), Advanced Reinforced Concrete Structures (17.5/20); structural dynamics and seismology; seminar (18/20) reviewing structural health monitoring methods.

### BSc in Civil Engineering
*Azad University, West Tehran Branch, Iran · Sep 2012 to Dec 2016 · GPA 15.84/20*

### Deep Dive into Blockchain, International Summer School
*University of Zurich, Switzerland · Jul 2026 · One month, online · Industry Scholarship (full fee waiver, CHF 1,000)*

## AI evaluation: experience

### Freelance Researcher, AI Evaluation for Structural Engineering
*Remote, freelance · Aug 2026 to present*

AI models are being tried for structural review without a clear measure of how often they get code checks right. I write expert review tasks from realistic reinforced concrete project documents and test Claude and Gemini models on them with my own open-source harness. On six tasks entered in the micro1 Eval Hackathon (Nov 2026), four current models passed 0 of 42 trials, and 13 of 42 with the cited standards available to look up.

### AI Trainer, Civil and Structural Engineering
*DataAnnotation (Surge AI) · Remote, freelance · Oct 2026 to Nov 2026*

AI agents misapply design rules in ways that simple tests miss. I spent more than 240 hours designing 20 realistic review tasks on US reinforced concrete (ACI 318, ASCE 7), each with an answer key checked against the code text and a written reason why each AI answer was right or wrong; 58 of 60 final model runs failed.

### Generalist Expert, Global Business
*Mercor · Remote, freelance · Aug 2026*

AI answers to business tasks can sound right and still be wrong. I rated them for accuracy, reasoning, instruction-following and usefulness, with a written reason for every rating.

## AI evaluation: projects

### Expert eval harness
*2026 · [github.com/sabaazdn73/expert-eval-harness](https://github.com/sabaazdn73/expert-eval-harness) · Python, Claude and Gemini APIs, GitHub Actions*

A single answer says little about how reliably a model handles expert work. The open-source harness runs each task several times per model and scores every answer item by item against the expert key, with pass@k, pass^k, confidence intervals and difficulty and quality gates. On the hackathon tasks two LLM judges from different model families agreed on 96% of items; every disagreement goes to a human expert.

### Task pipeline and method
*2026 · [tnega.app/eval](https://www.tnega.app/eval/) · [video walkthrough](https://www.youtube.com/watch?v=IWcEG7c-mQU) · JavaScript*

AI drafts task prompts and keys well but misses facts that change, such as the code edition a jurisdiction has adopted. My article [“Where the Human Belongs”](https://medium.com/@sabaazadegan/where-the-human-belongs-ab775c2fa3f7) sets out which steps the engineer must check; the pipeline page shows each hackathon task’s nine stages and results.

### RC Code Town
*2026 · [tnega.app/town](https://www.tnega.app/town/) · three.js*

Reviewers need to see where in a building an AI model tends to go wrong. RC Code Town shows six types of US concrete structures in 3D at true scale, with geometry from FEMA, FHWA and code sources; clicking a part shows the governing provisions and the errors AI models tend to make there (84 failure cards, 25 review scenarios). Some of my evaluation tasks are set on these buildings; an AI reviewer for structural drawings is in development on the same site.

### Review notebook
*2026 · [tnega.app/notebook](https://www.tnega.app/notebook/) · Python*

An evaluator has to know structural fundamentals to judge a model’s reasoning. Each section gives the idea, a worked example, a practice problem and a trap to test on AI models, with every number computed in a script; three modules so far: 82 sections, 85 figures, 24 harness tasks.

## Papers

### Can an AI-drafted review be signed? Language model errors in concrete design review
*Sole author · manuscript under review, ISEC-2027 (Pomona, California) · submitted Nov 2026*

A design review is only useful if an engineer can sign it. On six review tasks on fictional reinforced concrete projects (a submittal, a request for information or a delegated design), the paper classifies model errors by what they would mean in a signed review (life safety, durability or cost) and gives a checklist for the engineer of record. Even with the standards available, 15 of 25 answered trials on tasks with life-safety items missed at least one of them.

### Where language models fail in structural engineering review: expert-designed tasks and the code-edition trap
*Sole author · abstract under review, EG-ICE 2027 (Lund, Sweden) · submitted Nov 2026*

The same tasks, seen from the evaluation method. The failures came from choosing the wrong governing rule or code edition, not from arithmetic; the paper argues that the engineer’s part is to supply what lies outside the model, such as the real state of the project.

### Financial Damage Detection Index
*Sole author · Oct 2025 to Jan 2026 · DCC-GARCH*

Financial stress often shows only after large price moves. I applied the stiffness-based damage detection of structural health monitoring to company finances, with time-series models of market data. Accepted at the IFABS 2026 London Conference (review score 7.4/10); withdrawn before the conference.

## Engineering experience

### Graduate Researcher, Damage Detection in Bridges
*Kharazmi University, Iran · About 18 months within the MSc (Oct 2018 to Feb 2021)*

Damage changes a structure’s stiffness before it can be seen. I modelled damage in bridges in Abaqus as local stiffness loss and studied how it shifts their natural frequencies and mode shapes, the basis of vibration-based structural health monitoring.

### Site Civil Engineer (graduate trainee), Parvin mixed-use project
*Aghigh Naghsh-e-Jahan Investment Holding · Isfahan, Iran · May 2018 to Oct 2018*

The project needed reliable quantities and costs for a cast-in-place reinforced concrete building. I did the full quantity takeoff from the AutoCAD drawings and the cost estimate in Excel, supervised foundation and rebar work, and supported the project manager with planning.

## Other work: mini dApps and mini apps

- **Tnega Finance** ([tnega.app/finance](https://www.tnega.app/finance)): what a tokenised stock really costs to buy, across 7,279 versions of 1,378 stocks and ETFs from five issuers on seven chains; its MCP server lets an AI assistant prepare a trade that the user signs in their own wallet.
- **Cross-Border (F2F)** ([f2f-uzh.vercel.app](https://f2f-uzh.vercel.app)): every compliance and routing decision of a cross-border transfer recorded on Hedera; I led a team from four countries at the University of Zurich summer school and extended it for ETHGlobal Lisbon 2026.
- **TrustCycle** ([trustcycle.tech](https://trustcycle.tech)): academic recommendation letters that a reader can verify on IOTA; ranked 22 of 66 at the MasterZ and IOTA Web3 hackathon.
- **BIM practice** ([tnega.app/bim](https://www.tnega.app/bim/)): a free course modelling one reinforced concrete building in 32 exercises, with an IFC checker that runs in the browser.
- **Hava** ([tnega.app/hava](https://www.tnega.app/hava/)): drawing in the air with your hands on a video call; the hand tracking runs in the browser.

## Awards and programmes

- Partner prize (1,000 USDC), ETHGlobal Lisbon 2026, for Cross-Border (F2F).
- IFABS Grant for Young Researchers (GBP 450 fee waiver), IFABS 2026 London Conference.
- Google for Startups Immersion EMEA, powered by Antler (accepted, Oct 2026); Solana Fall School (Oct 2026).
- Google Cloud Professional Agentic Architect, Special Edition cohort (in progress since Nov 2026).
- Anthropic Claude Academy: Introduction to Evals and AI Fluency (in progress); Mercor: Introduction to Agents.

## Skills

- **AI and programming:** Claude Code, Claude and Gemini APIs, tool calling and MCP servers; LLM evaluation (task and rubric design, LLM judges, pass@k); Python (NumPy, pandas, scikit-learn) and SQL at a basic level; Git and GitHub Actions.
- **Engineering:** ETABS, SAFE and Abaqus (about a year of modelling and analysis), AutoCAD; ACI 318 and ASCE 7; Eurocodes (self-study).
- **Languages:** English (professional), Persian (native), Portuguese (basic). **Photography:** since 2017, mainly architectural ([portfolio](https://www.tnega.app/photography/)).
