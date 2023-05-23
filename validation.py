#!/usr/bin/env python

"""Script used to test the network with batfish"""

from pybatfish.client.commands import *
from pybatfish.question import load_questions
from pybatfish.client.asserts import (
    assert_no_duplicate_router_ids,
    assert_no_incompatible_ospf_sessions,
    assert_no_undefined_references,
)
from rich.console import Console


console = Console(color_system="truecolor")


def test_duplicate_rtr_ids(snap):
    """Testing for duplicate router IDs"""
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for duplicate router IDs[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_duplicate_router_ids(
        snapshot=snap,
        protocols={"ospf", "bgp"},
    )
    console.print(
        ":green_heart: [bold green]No duplicate router IDs found[/bold green] :green_heart:"
    )




def test_ospf_compatibility(snap):
    """Testing for incompatible OSPF sessions"""
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for incompatible OSPF sessions[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_incompatible_ospf_sessions(
        snapshot=snap,
    )
    console.print(
        ":green_heart: [bold green]All OSPF sessions compatible![/bold green] :green_heart:"
    )




def test_undefined_references(snap):
    """Testing for any undefined references"""
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for undefined references[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_undefined_references(
        snapshot=snap,
    )
    console.print(
        ":green_heart: [bold green]No undefined refences found![/bold green] :green_heart:"
    )


def main():
    """init all the things"""
    NETWORK_NAME = "pfe"
    SNAPSHOT_NAME = "snapshot01"
    SNAPSHOT_DIR = "./snapshots"
    bf_session.host = "127.0.0.1"
    bf_set_network(NETWORK_NAME)
    init_snap = bf_init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)
    load_questions()
    test_duplicate_rtr_ids(init_snap)
    test_ospf_compatibility(init_snap)
    test_undefined_references(init_snap)


if __name__ == "__main__":
    main()
