from redbot.core import commands, Config, app_commands
from datetime import datetime, timedelta
import random
import discord

from .responses import BED_LINES, HR_LINES, RATINGS


class SleepCorp(commands.Cog):
    """SIN Corporation Sleep Tracking"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=4242424242)
        default_user = {
            "sleep_time": None,
        }
        self.config.register_user(**default_user)

    def _parse_time(self, time_str: str):
        """Parse HH:MM into a datetime for today."""
        try:
            parsed = datetime.strptime(time_str, "%H:%M")
            now = datetime.now()
            return now.replace(hour=parsed.hour, minute=parsed.minute, second=0, microsecond=0)
        except ValueError:
            return None

    @app_commands.command(name="sleep", description="Log when you went to bed.")
    async def sleep(self, interaction: discord.Interaction, time: str = None):
        user = interaction.user

        if time:
            now = self._parse_time(time)
            if now is None:
                await interaction.response.send_message(
                    "Invalid time format. Please use HH:MM, for example `02:37`.",
                    ephemeral=True
                )
                return
        else:
            now = datetime.now()

        await self.config.user(user).sleep_time.set(now.timestamp())

        line = random.choice(BED_LINES)
        await interaction.response.send_message(
            f"🌙 **SIN CORP SLEEP LOG**\n"
            f"{user.mention} went to bed at **{now.strftime('%H:%M')}**.\n"
            f"{line}"
        )

    @app_commands.command(name="awake", description="Log when you woke up.")
    async def awake(self, interaction: discord.Interaction, time: str = None):
        user = interaction.user
        data = await self.config.user(user).sleep_time()

        if not data:
            await interaction.response.send_message(
                "SIN Corporation has no sleep data for this employee.",
                ephemeral=True
            )
            return

        start = datetime.fromtimestamp(data)

        if time:
            end = self._parse_time(time)
            if end is None:
                await interaction.response.send_message(
                    "Invalid time format. Please use HH:MM, for example `11:42`.",
                    ephemeral=True
                )
                return
        else:
            end = datetime.now()

        if end < start:
            end = end + timedelta(days=1)

        duration = end - start
        hours = duration.total_seconds() / 3600

        if hours < 4:
            rating = 0
        elif hours < 6:
            rating = 2
        elif hours < 8:
            rating = 3
        else:
            rating = 5

        stars = "★" * rating + "☆" * (5 - rating)

        report = (
            f"🌙 **SIN CORP SLEEP EVALUATION**\n"
            f"Employee: {user.mention}\n"
            f"Bedtime: {start.strftime('%H:%M')}\n"
            f"Wake Time: {end.strftime('%H:%M')}\n"
            f"Duration: {round(hours, 2)} hours\n\n"
            f"Rating: {stars}\n"
            f"{random.choice(RATINGS[rating])}\n"
            f"{random.choice(HR_LINES)}"
        )

        await self.config.user(user).sleep_time.set(None)
        await interaction.response.send_message(report)

    @app_commands.command(name="bedtime", description="Check last recorded bedtime.")
    async def bedtime(self, interaction: discord.Interaction, user: discord.User = None):
        target = user or interaction.user
        data = await self.config.user(target).sleep_time()

        if not data:
            await interaction.response.send_message(
                "SIN Corporation has no data for this employee.",
                ephemeral=True
            )
            return

        start = datetime.fromtimestamp(data)
        await interaction.response.send_message(
            f"🌙 {target.mention} went to bed at **{start.strftime('%H:%M')}**."
        )


async def setup(bot):
    await bot.add_cog(SleepCorp(bot))
