from src.persistence.repository import Repository


def populate_db(repo: Repository) -> None:
    """Populates the db with a random country"""
    from src.models.country import Country

    countries = [
        Country(name="Uruguay", code="UY"),
    ]

    for country in countries:
        repo.save(country)

    print("Memory DB populated")
