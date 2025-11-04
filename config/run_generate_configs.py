from config.config_generation import generate_and_save_all, GENERATORS
from config.generators.app_config_gen import AppConfigGenerator
from config.generators.auth_routes_config_gen import AuthRoutesConfigGenerator

# Register your configurations here:
GENERATORS.append(AppConfigGenerator())
GENERATORS.append(AuthRoutesConfigGenerator())


if __name__ == "__main__":
    # Generate and save all configs for all environments
    generate_and_save_all()
    print("All configuration files have been generated successfully!")
