from crewai import Task
from textwrap import dedent


class DevTasks:
    """
    """

    def __int__(self):
        self.filepath = None

    def which_types_of_devices_get_the_most(self, agent, tools):
        """
        * Which types of devices get the most ad clicks, ranked from highest to lowest
        Args:
            tools:
            agent:

        Returns:

        """
        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def get_insight_from_data(self, agent, description, files, **kwargs):
        """
        * Build a model to predict ad click probabilities
        Args:
            tools:
            agent:
        Returns:

        """
        return Task(
            description=dedent(
                f"\n"
                f"{description}  \n"
                f"{self.__stack()}  \n"
                f"{kwargs or ''}\n"
            ),
            agent=agent
        )

    def build_model_to_predict(self, agent):
        """
        * Build a model to predict ad click probabilities
        Args:
            agent:

        Returns:

        """
        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def rank_features(self, agent, influences):
        """
        * Rank features by their influence on ad clicks

        Args:
            agent:

        Returns:

        """
        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def what_are_the_best_times_of_day(self, agent):
        """
        * What are the best times of day for ad clicks? List the top 5 hours by their click success rate
        Args:
            agent:

        Returns:

        """

        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def what_are_the_best_days_of_week(self, agent):
        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def improve_the_model(self, agent):
        """
        Improve the model's accuracy in predicting
        Args:
            agent:

        Returns:

        """
        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def discover_patterns(self, agent):
        """
        Discover patterns in user events like signups and registrations
        """
        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def display_the_top_websites(self, agent, values=15):
        """
        Display the top 15 websites where our ads receive the most clicks
        Args:
            agent:

        Returns:

        """

        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def identify_the_top_10(self, agent):
        """
            * Identify the top 10 geographic areas where our ads perform best in terms of click rates
        """

        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def identify_how_well_the_click_prediction_model(self, agent):
        """
        Assess how well the click prediction model works
        """
        return Task(
            description=dedent(
                """
                """
            ),
            agent=agent,
        )

    def find_the_top_factors_that_drive(self, agent):
        """
        * Find the top factors that drive ad clicks
        Args:
            agent:

        Returns:

        """
        return Task(
            description=dedent(
                """
Complete goal: Find the top factors that drive ad clicks
{self.__stack()}
"""
            ),
            agent=agent,
        )

    def __stack(self):
        return "You can use all available libraries for Python."

    def get_files_from_dir(self, agent, description, directory):
        return Task(
            description=dedent(
                f"{description}  \n"
                f"{directory or ''}\n"
            ),
            agent=agent
        )

    def get_data_description(self, agent, description, files):
        return Task(
            description=dedent(
                f"{description}  \n"
                f"{files or ''}\n"
            ),
            agent=agent
        )
