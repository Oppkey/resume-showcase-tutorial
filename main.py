import flet as ft
from dataclasses import dataclass


@dataclass
class ShowOff:
    name: str
    image_path: str = None
    highlight: str = ""
    outcome: str = ""
    details: str = ""


SHOWOFF_LIST = [
    ShowOff(
        "overview",
        "jesse.jpeg",
        highlight="Fluent in Python and Japanese",
        outcome="Stanford University alumnus who is committed to learning on the job and growing as a developer.",
        details="I have completed the Oppkey Industy Projects with Python course and am ready to apply my skills to a real-world project.",
    ),
    ShowOff("demo", "python_logo2.png", highlight="I'd like to demo and talk about my Python app with advanced UI components", outcome="My app that can be deployed on mobile, desktop or web", details="Let's discuss the work I've already done with Declarative UI using Flet with Flutter widgets and a FastAPI Uvicorn backend"),
    ShowOff("experience", "chip.png", highlight="I have worked in open source and developer communities, and I like testing apps and documenting my steps. ", outcome="When I contribute the results to the community, I both helps me progress faster and helps the community grow.", details="I helped manage the RICOH THETA developer community and helped support and test the RICOH THETA SDK for over 8 years."),
    ShowOff("education", "stanford-logo2.png", highlight="I have long-term connections with engineers at Stanford and Japan, and this could help any internship I get.", outcome="私はビジネス、技術、法律といった場面で日本語を話すことができます。I can speak Japanese in business, technical, and legal situations.", details="I like libraries and manuals!"),
    ShowOff("skills", "fastopp_logo.png", highlight="I have skills in Python, Flet, Flutter, FastAPI, and Uvicorn. I can provide a live demo or video of some of my recent work.", outcome="I like to learn new things and apply them to real-world projects.", details="I hope to work more with new Python tools like uv and ruff."),
    ShowOff("interests", "rpi.jpg", highlight="I am interested in AI, Machine Learning, and Cloud Computing.", outcome="I have built Raspberry Pi projects that my wife raves about!", details="I contributed to the Magic Mirror community and created a mirror in the entranceway to my appartment that displays the time, weather, and news."),
]

print(f"ShowOff string representation: {SHOWOFF_LIST[0]}")

print(f"Contents of index 0 and 1 the same? {SHOWOFF_LIST[0] == SHOWOFF_LIST[1]}")


@ft.component
def App():
    showoffs: dict[str, ShowOff] = {showoff.name: showoff for showoff in SHOWOFF_LIST}

    showoff: ShowOff
    showoff, set_showoff = ft.use_state(showoffs["overview"])
    snackbar_key, set_snackbar_key = ft.use_key = ft.use_state(0)

    def handle_selection(e):
        set_showoff(showoffs[e.control.value])
        set_snackbar_key(snackbar_key + 1)
        print(e.control.value)

    def change_snackbar_message(showoff_name: str):
        message = f"The story of {showoff_name} begins!"

        match showoff_name:
            case "overview":
                message = "As co-founder of Oppkey, I build community-led growth engines for FastAPI/Python, PaaS, and backend tooling: positioning, proof, and programs that convert."
            case "demo":
                message = "Fullstack Python experience with Flutter-based frontend. Can modify for use with React and other frontends. I'm always learning more!"
            case "experience":
                message = "I've worked in Silicon Valley for over 2 decades. I like solving problems and building things."
            case "education":
                message = "I have a Master's from Stanford University, but that was just the start of my journey. I like learning on the job and growing as a developer."
            case "skills":
                message = "Skills include: FastAPI, Python, PaaS, Flet, Flutter, and Uvicorn."
            case "interests":
                message = "Interests include: AI, Machine Learning, and new Python tools. I have also built several Raspberry Pi projects including a Magic Mirror that displays the time, weather, and news."

        return message

    return ft.Column(
        controls=[
            ft.Text(value="Jesse Casman", size=30),
            ft.Text(value="Looking for software engineering internship. I am excited to intern at a company that is building products that use AI and need someone who is energetic and has a good grasp of Python and UI development. I have applications that I can demo. Let's talk!\n", size=15),
            ft.Dropdown(
                label="resume sections",
                options=[
                    ft.DropdownOption(text=showoff_item.name)
                    for showoff_item in showoffs.values()
                ],
                value=showoff.name,
                on_select=handle_selection,
            ),
            ft.Row(
                [
                    ft.Image(src=showoff.image_path),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(
                                            "Highlight: ",
                                            style=ft.TextStyle(
                                                weight=ft.FontWeight.BOLD
                                            ),
                                        ),
                                        ft.TextSpan(showoff.highlight),
                                    ],
                                    size=22,
                                ),
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(
                                            "Outcome: ",
                                            style=ft.TextStyle(
                                                weight=ft.FontWeight.BOLD
                                            ),
                                        ),
                                        ft.TextSpan(showoff.outcome),
                                    ],
                                    size=22,
                                ),
                                ft.Text(
                                    spans=[
                                        ft.TextSpan(
                                            "Details: ",
                                            style=ft.TextStyle(
                                                weight=ft.FontWeight.BOLD
                                            ),
                                        ),
                                        ft.TextSpan(showoff.details),
                                    ],
                                    size=22,
                                ),
                            ],
                        ),
                        padding=20,
                        width=600,
                    ),
                ],
            ),
            ft.SnackBar(
                content=ft.Text(change_snackbar_message(showoff.name)),
                key=f"snackbar_{snackbar_key}",
                open=snackbar_key > 0,
                on_dismiss=lambda e: set_snackbar_key(0),
            ),
        ],
    )


ft.run(lambda page: page.render(App))
