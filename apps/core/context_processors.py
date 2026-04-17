def nav_links(request):
    return {
        "nav_links": [
            {"label": "Solutions", "url": "#solutions", "name": "home"},
            {"label": "Capabilities", "url": "#capabilities", "name": "home"},
            {"label": "Process", "url": "#process", "name": "home"},
            {"label": "Insights", "url": "#insights", "name": "home"},
        ]
    }


def methodology_steps(request):
    return {
        "methodology_steps": [
            {
                "number": "01",
                "title": "Discovery",
                "description": "In-depth technical audit and stakeholder alignment to define the architectural scope.",
            },
            {
                "number": "02",
                "title": "Strategy",
                "description": "Developing the technical roadmap and selecting the optimal stack for your specific goals.",
            },
            {
                "number": "03",
                "title": "Implementation",
                "description": "Agile engineering cycles with continuous integration and automated quality assurance.",
            },
            {
                "number": "04",
                "title": "Optimization",
                "description": "Continuous monitoring and performance tuning to maximize ROI and operational efficiency.",
            },
        ]
    }
