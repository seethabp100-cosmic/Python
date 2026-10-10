from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from pathlib import Path

outputdir = Path("output")
outputdir.mkdir(exist_ok=True)

#out = "/mnt/data/AI_Engineering_MVP_Technology_Learning_Roadmap_Structured.pdf"
out = outputdir / "AI_Engineering_MVP_Technology_Learning_Roadmap_Structured.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=20, leading=24, alignment=TA_CENTER, spaceAfter=8))
styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontName="Helvetica",
    fontSize=9.5, leading=13, alignment=TA_CENTER, textColor=colors.HexColor("#555555"), spaceAfter=12))
styles.add(ParagraphStyle(name="H1Road", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=15, leading=18, spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyRoad", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=8.8, leading=12.2, spaceAfter=4))
styles.add(ParagraphStyle(name="Cell", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=7.2, leading=9.1, spaceAfter=0))
styles.add(ParagraphStyle(name="CellHead", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=7.4, leading=9.2, textColor=colors.white, spaceAfter=0))

def P(text, style="BodyRoad"):
    return Paragraph(text, styles[style])

def cell(text, head=False):
    return P(text, "CellHead" if head else "Cell")

def road_table(headers, rows, widths):
    data = [[cell(h, True) for h in headers]]
    data += [[cell(x) for x in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#30364F")),
        ("GRID",(0,0),(-1,-1),0.35,colors.HexColor("#B8BEC9")),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),4), ("RIGHTPADDING",(0,0),(-1,-1),4),
        ("TOPPADDING",(0,0),(-1,-1),4), ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))
    for r in range(2, len(data), 2):
        t.setStyle(TableStyle([("BACKGROUND",(0,r),(-1,r),colors.HexColor("#F5F6F8"))]))
    return t

# doc = SimpleDocTemplate(out, pagesize=A4, rightMargin=16*mm, leftMargin=16*mm,
#                         topMargin=14*mm, bottomMargin=15*mm)
doc = SimpleDocTemplate(
    str(out),
    pagesize=A4,
    rightMargin=16*mm,
    leftMargin=16*mm,
    topMargin=14*mm,
    bottomMargin=15*mm
)
story = []

# Page 1
story += [
    P("AI Engineering — Technology & Learning Roadmap", "CoverTitle"),
    P("A phased learning and development plan showing what technologies and AI engineering concepts are introduced at each level, why they are needed, and what you will learn by building one product.", "Subtitle"),
    P("Project Goal", "H1Road"),
    P("Build an AI Knowledge & Document Assistant where a user can ask questions, upload documents, retrieve relevant knowledge, receive grounded AI answers, and progressively use controlled tools. The same product evolves from a console application into a backend service, RAG system, agent workflow, observable production service, and React web application."),
    P("Recommended Development Order", "H1Road"),
    road_table(["Phase","Level","Main outcome","Technologies"], [
        ["1","Python Foundation","Production-quality Python application works","Python, venv, typing, pytest, Git"],
        ["2","Backend","AI service works through REST API","FastAPI, Pydantic, PostgreSQL"],
        ["3","ML Foundations","Understand data/model/evaluation lifecycle","NumPy, pandas, scikit-learn"],
        ["4","Deep Learning","Understand neural-network fundamentals","PyTorch, tensors, training"],
        ["5","LLM Engineering","Reliable LLM application works","LLM API, prompts, structured output, tools"],
        ["6","RAG","Documents can be queried with grounded answers","Embeddings, vector DB, retrieval, reranking"],
        ["7","Agents","Controlled multi-step tool workflow works","Tools, state, workflows, guardrails"],
        ["8","Production AI","Observable and deployable AI system","Docker, CI/CD, evaluation, tracing, cloud"],
        ["9","Frontend","Complete usable AI product","React, TypeScript, streaming UI"],
    ], [13*mm,35*mm,68*mm,58*mm]),
    Spacer(1,7),
    P("Phase 1 — Python Engineering", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["Python project structure","Modules, packages, src layout and clean separation of responsibilities.","Start"],
        ["venv + pip / pyproject","Isolate project dependencies and understand Python package management.","Start"],
        ["Typing + dataclasses","Make application contracts explicit and easier to maintain.","Start"],
        ["Exceptions + logging","Handle failures predictably and make applications diagnosable.","Start"],
        ["pytest","Test functions, services and failure cases instead of relying only on manual execution.","Start"],
        ["HTTP + JSON","Understand protocol concepts before building AI APIs.","Start"],
        ["async/await","Understand concurrency for I/O-heavy AI/API workloads.","After basics"],
    ], [48*mm,103*mm,23*mm]),
    P("Phase 2 — Backend & Data", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["FastAPI","Build typed REST endpoints and expose the Python application as a service.","After Python"],
        ["Pydantic","Validate request/response data and create explicit API contracts.","Same"],
        ["PostgreSQL","Persist users, conversations, documents and application metadata.","Same"],
        ["Service architecture","Separate API, business logic, AI orchestration and persistence.","Same"],
        ["API testing","Test endpoints and integration paths before adding AI complexity.","Same"],
    ], [48*mm,103*mm,23*mm]),
    PageBreak()
]

# Page 2
story += [
    P("Phase 3 — Data & Machine Learning", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["NumPy","Arrays, vectorized computation and numerical foundations used by ML tooling.","After API"],
        ["pandas","Load, clean, transform and inspect structured datasets.","Same"],
        ["Statistics","Distributions, averages, variance, probability and sampling intuition.","Same"],
        ["Train/validation/test","Separate learning from model selection and final evaluation.","Same"],
        ["scikit-learn","Build classical ML pipelines and learn preprocessing, training and evaluation.","Same"],
        ["Metrics","Understand accuracy, precision, recall, F1, ROC-AUC and confusion matrices.","Same"],
        ["Data leakage","Recognize when training information contaminates evaluation.","Same"],
    ], [48*mm,103*mm,23*mm]),
    P("Phase 4 — Deep Learning with PyTorch", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["Tensors","Core data structure for neural-network computation.","After ML"],
        ["Neural networks","Layers, activations, parameters and forward passes.","Same"],
        ["Loss + optimization","Understand what training minimizes and how weights change.","Same"],
        ["Backpropagation/autograd","Understand how gradients are calculated for learning.","Same"],
        ["Datasets/data loaders","Feed training and evaluation data efficiently.","Same"],
        ["Model persistence","Save/load trained models and separate training from inference.","Same"],
    ], [48*mm,103*mm,23*mm]),
    P("Phase 5 — LLM Engineering", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["LLM API","Call a foundation model from Python and handle model responses.","After ML basics"],
        ["Tokens/context","Understand input size, context limits and context selection.","Same"],
        ["Prompt design","Define reliable instructions, constraints and output requirements.","Same"],
        ["Structured output","Return validated data instead of relying on free-form text.","Same"],
        ["Streaming","Send generated output incrementally for responsive UI.","Same"],
        ["Tool/function calling","Let the model request controlled application functions.","Same"],
        ["AI failure handling","Handle rate limits, timeouts, invalid output and provider failures.","Same"],
        ["Cost/latency","Track token usage, response time and model-selection trade-offs.","Same"],
    ], [48*mm,103*mm,23*mm]),
    P("Phase 6 — RAG", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["Document ingestion","Read PDF, Markdown, HTML or text and normalize content.","After LLM"],
        ["Chunking","Split large documents into retrievable pieces with useful metadata.","Same"],
        ["Embeddings","Represent text as vectors for semantic similarity search.","Same"],
        ["Vector database","Store and retrieve embedding vectors efficiently.","Same"],
        ["Retrieval","Select relevant chunks before generation instead of sending everything.","Same"],
        ["Hybrid search","Combine semantic and lexical retrieval when exact terms matter.","Advanced"],
        ["Reranking","Improve ordering of retrieved candidates before generation.","Advanced"],
        ["Citations","Show which source chunks support an answer.","Same"],
    ], [48*mm,103*mm,23*mm]),
    PageBreak()
]

# Page 3
story += [
    P("Phase 7 — Agents & Tool-Using Systems", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["Workflow vs agent","Know when deterministic steps are enough and when dynamic tool selection is useful.","After RAG"],
        ["Tool definitions","Expose narrowly scoped functions with clear inputs and outputs.","Same"],
        ["State","Persist information required across multiple workflow steps.","Same"],
        ["Decision loop","Understand request → decide → tool → observe → continue/stop.","Same"],
        ["Guardrails","Restrict dangerous, expensive or invalid tool/model behavior.","Same"],
        ["Human approval","Require confirmation before side-effecting actions.","Production"],
        ["Agent framework","Use a framework only after understanding the underlying workflow.","Advanced"],
        ["MCP concepts","Understand standardized tool/context integration patterns.","Advanced"],
    ], [48*mm,103*mm,23*mm]),
    P("Phase 8 — Evaluation & LLMOps", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["Evaluation dataset","Create representative questions and expected behavior before changing prompts/models.","After RAG"],
        ["Retrieval evaluation","Measure whether required source information is retrieved.","Same"],
        ["Answer evaluation","Measure correctness, grounding and usefulness with repeatable cases.","Same"],
        ["Regression testing","Detect when prompt/model/retrieval changes break previous behavior.","Same"],
        ["Tracing","Follow a request across API, retrieval, tools, model and database.","Production"],
        ["Logging/metrics","Track errors, latency, tokens, cost and throughput.","Production"],
        ["Model/prompt comparison","Compare changes using the same evaluation set rather than intuition.","Advanced"],
    ], [48*mm,103*mm,23*mm]),
    P("Phase 9 — Production Engineering", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["Docker","Package the application and runtime dependencies consistently.","After MVP"],
        ["Docker Compose","Run backend, database and supporting services locally.","Same"],
        ["CI/CD","Automate tests, builds and deployment.","Same"],
        ["Secrets/config","Keep API keys and credentials outside source code.","Same"],
        ["Rate limiting","Control abuse, provider limits and operating cost.","Production"],
        ["Caching","Reduce repeated expensive database/provider operations.","Production"],
        ["Cloud deployment","Learn networking, runtime configuration, storage and scaling.","Advanced"],
        ["Security","Authentication, authorization, input validation and safe tool execution.","Production"],
    ], [48*mm,103*mm,23*mm]),
    P("Phase 10 — Frontend / Product Layer", "H1Road"),
    road_table(["Technology / concept","What you learn / why it exists","When"], [
        ["React + TypeScript","Build the product UI around the AI service.","After backend"],
        ["Streaming chat UI","Display model responses progressively.","Same"],
        ["Document upload","Send documents into the ingestion/RAG pipeline.","Same"],
        ["Citations/source panel","Expose retrieved evidence to the user.","Same"],
        ["Tool status","Show when the assistant is retrieving or invoking a tool.","Same"],
        ["Auth/session","Protect conversations and user resources.","Production"],
    ], [48*mm,103*mm,23*mm]),
    PageBreak()
]

# Page 4
story += [
    P("Suggested MVP Architecture", "H1Road"),
    P("The architecture should evolve only when the project requirement justifies the next technology."),
    road_table(["Stage","Architecture","Purpose"], [
        ["Initial MVP","Console → Python service → local files","Learn Python fundamentals without infrastructure noise."],
        ["Backend MVP","React → FastAPI → PostgreSQL","Learn REST, validation, persistence and application layering."],
        ["LLM version","FastAPI → AI service → LLM API → PostgreSQL → React","Introduce model integration while keeping the application deterministic around it."],
        ["RAG version","Document → parser → chunker → embeddings → vector DB → retriever → LLM","Ground answers in external/private knowledge."],
        ["Agent version","User → AI workflow → retrieval/tools → approval → response","Add controlled multi-step behavior."],
        ["Production version","React → FastAPI → workers → DB/vector DB → AI/tools + evaluation/observability","Handle reliability, security and operations."],
    ], [30*mm,100*mm,54*mm]),
    P("Learning Milestones", "H1Road"),
    road_table(["Milestone","Definition of done"], [
        ["1","A Python console application is structured, tested, logged and packaged cleanly."],
        ["2","A FastAPI service exposes validated endpoints and persists application data."],
        ["3","A small ML project can be trained, evaluated and explained using appropriate metrics."],
        ["4","An LLM assistant produces structured responses and handles provider failures."],
        ["5","Documents can be ingested, chunked, embedded and searched."],
        ["6","RAG answers include relevant retrieved sources and have repeatable evaluation cases."],
        ["7","A controlled agent/workflow can use approved tools and requires confirmation for side effects."],
        ["8","The system records quality, latency, token/cost and failure information."],
        ["9","The backend is containerized, tested and deployable."],
        ["10","React provides chat, upload, source citations and live status."],
    ], [27*mm,157*mm]),
    P("Recommended Order", "H1Road"),
    P("1. Python fundamentals and software engineering → 2. FastAPI, REST and PostgreSQL → 3. NumPy, pandas and ML fundamentals → 4. PyTorch → 5. LLM APIs and structured output → 6. RAG → 7. Agents/tool workflows → 8. Evaluation and observability → 9. Docker/cloud/security → 10. React product UI."),
    P("Key principle: build one working vertical slice first. Do not introduce RAG, agents, Docker, vector databases and multiple AI frameworks simultaneously. Each phase should solve a real requirement of the product before the next technology is added."),
    P("Daily Learning Model", "H1Road"),
    road_table(["Daily time","Activity","Output"], [
        ["15 min","Concept: Why / What / How","Short notes and one diagram."],
        ["20 min","Small implementation","Working isolated example."],
        ["35–50 min","Main project","One incremental feature."],
        ["15 min","Testing/debugging","Tests + failure handling."],
        ["10 min","Engineering notes","Decision, alternative, trade-off, next step."],
    ], [30*mm,62*mm,92*mm]),
    PageBreak()
]

# Page 5
story += [
    P("Technology Decision Framework", "H1Road"),
    P("For every technology introduced in the project, answer these questions before using it:"),
    road_table(["Question","What you should be able to explain"], [
        ["Why?","What concrete project problem does this technology solve?"],
        ["What?","What is the technology/concept and what abstraction does it provide?"],
        ["How?","How does it work at a useful engineering level?"],
        ["Why this option?","What alternatives exist and what trade-offs matter here?"],
        ["Failure cases?","What happens with invalid input, timeout, cost, stale data or provider failure?"],
        ["Testing?","How do we prove the component works and does not regress?"],
        ["Production?","How do security, observability, scalability and cost change the design?"],
    ], [42*mm,142*mm]),
    P("Daily / Weekly Schedule", "H1Road"),
    P("<b>Recommended:</b> 1.5–2 hours/day, 6 days/week. Use one day for review, refactoring or rest. At this pace, the full roadmap is approximately 8–10 months. The first pass is deliberately broad; deeper specialization can follow based on the AI role you target."),
    road_table(["Week pattern","Focus"], [
        ["Mon–Tue","Learn concept + implement small examples."],
        ["Wed–Thu","Add a project feature using the concept."],
        ["Fri","Integration, tests and failure handling."],
        ["Sat","Refactor, document architecture and record trade-offs."],
        ["Sun","Rest or optional catch-up."],
    ], [45*mm,139*mm]),
    P("Final Outcome", "H1Road"),
    P("By completing the roadmap, you should be able to take an AI application from <b>Python code → API → database → ML understanding → LLM → RAG → tools/agents → evaluation → production deployment → frontend</b>, while explaining the engineering decisions at every stage."),
    P("The objective is not to memorize AI libraries. The objective is to become capable of answering: <b>What problem are we solving? Why this architecture? What alternatives exist? How do we measure quality? What happens when the model fails? What does it cost? How do we secure, test, deploy and monitor it?</b>"),
    P("Roadmap scope", "H1Road"),
    P("This document is an MVP learning roadmap. It intentionally postpones foundation-model training, advanced GPU/kernel optimization, multi-cloud mastery and research-level mathematics until a specific role or project requires them.")
]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawRightString(A4[0]-16*mm, 7.5*mm,
                           f"AI Engineering — Technology & Learning Roadmap    Page {doc.page}")
    canvas.restoreState()

#doc.build(story, onFirstPage=footer, onLaterPages=footer)
doc.build(
    story,
    onFirstPage=footer,
    onLaterPages=footer
)
print(out)
