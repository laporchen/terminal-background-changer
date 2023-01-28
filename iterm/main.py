#!/usr/bin/env python3

import iterm2
import os
import subprocess

folder_location = os.getenv("ITERMIMAGEFOLDER")


def selectBackground(folder_location: str) -> str:
    res = subprocess.run([f"find '{folder_location}' | fzf"],stdout=subprocess.PIPE,text=True,shell=True)
    return res.stdout.replace("\r","").replace("\n","")

async def main(connection):
    app = await iterm2.async_get_app(connection) 
    if app == None:
        return

    async def changeBackground(session):
        global folder_location
        image_location = ""

        if not folder_location:
            return
        if not session:
            return

        while True:
            image_location = selectBackground(folder_location)
            if len(image_location) == 0:
                break
            new_profile = iterm2.LocalWriteOnlyProfile()
            new_profile.set_background_image_location(image_location)
            await session.async_set_profile_properties(new_profile)


        return

    profile = None
    profileName = os.getenv("PROFILENAME")
    if not profileName:
        profileName = "Default"

    partialProfiles = await iterm2.PartialProfile.async_query(connection)
    for partial in partialProfiles:
        if partial.name == profileName:
            profile = await partial.async_get_full_profile()

     
    if not profile:
        error = iterm2.Alert("Cannot get your profile.", "")
        await error.async_run(connection)
        return

    if not folder_location:
        error = iterm2.Alert("Environment variable is not set.", "Please add 'ITERMIMAGEFOLDER=PathToFolder' to your environment variable.")
        await error.async_run(connection)
        return

    if app.current_terminal_window and app.current_terminal_window.current_tab:
        await changeBackground(app.current_terminal_window.current_tab.current_session)
    return



iterm2.run_until_complete(main)

