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


def testimonials(request):
    return {
        "testimonials": [
            {
                "quote": "The engineering rigor LGS brought to our cloud migration was unparalleled. They didn't just move our workloads; they completely re-imagined how our global data infrastructure operates. They are the benchmark for technical partnership.",
                "name": "Marcus Sterling",
                "title": "Chief Technology Officer, Global Logistics Corp",
                "avatar": "https://i.pravatar.cc/48?img=57",
            },
            {
                "quote": "LGS didn't just deliver a system — they delivered confidence. Their architectural approach gave us the scalability we needed to grow threefold without a single incident. Truly world-class engineers.",
                "name": "Sandra Voss",
                "title": "VP of Engineering, Meridian Financial",
                "avatar": "https://i.pravatar.cc/48?img=47",
            },
            {
                "quote": "From discovery to deployment, the LGS team operated with a level of precision and transparency we've never seen from a technology partner. They are now an extension of our own team.",
                "name": "David Okoro",
                "title": "Head of Digital, Nexus Retail Group",
                "avatar": "https://i.pravatar.cc/48?img=12",
            },
            {
                "quote": "The AI pipeline LGS built for us processes over 2 million records daily with 99.97% accuracy. That's not a vendor relationship — that's a strategic advantage.",
                "name": "Priya Nambiar",
                "title": "Chief Data Officer, Orion Healthcare",
                "avatar": "https://i.pravatar.cc/48?img=23",
            },
        ]
    }


def clients(request):
    return {
        "clients": [
            {"name": "Compreline Insurance Consultancy Inc."},
            {"name": "Uni-Vanguard Insurance Agency Inc."},
            {"name": "RAKKII AUTO SERVICE"},
        ]
    }
