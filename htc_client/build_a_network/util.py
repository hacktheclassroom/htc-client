from build_a_network.entity import SelectableAndDraggableBlock, DraggableBlock, BasicBlock
import math
import pygame


class BlockParser(object):
    def __init__(self, blockgroup_list):
        self.connected = []
        self.placed = []
        self.places = []
        self.blockgroup_list = blockgroup_list

    def _populate(self):
        if not self.blockgroup_list:
            return

        def add_block_to_list(blockgroup, l):
            for block in blockgroup:
                l.append(block)
            return l

        for blockgroup in self.blockgroup_list:
            if len(blockgroup) > 0:
                if isinstance(list(blockgroup)[0], SelectableAndDraggableBlock):
                    add_block_to_list(blockgroup, self.connected)
                elif isinstance(list(blockgroup)[0], DraggableBlock):
                    add_block_to_list(blockgroup, self.placed)
                elif isinstance(list(blockgroup)[0], BasicBlock):
                    add_block_to_list(blockgroup, self.places)

        self.blockgroup_list = None
        return self

    def parse(self):
        self._populate()
        connect_map = {}
        for connect in self.connected:
            if connect.joined_to and connect.name != connect.joined_to.name:
                connect_map[connect.name] = connect.joined_to.name
        placed_map = {}
        for place in self.places:
            for placedb in self.placed:
                if placedb.rect.colliderect(place.rect):
                    placed_map[placedb.name] = place.name
            for connectb in self.connected:
                if connectb.rect.colliderect(place.rect):
                    placed_map[connectb.name] = place.name
        flags = []
        for k, v in connect_map.items():
            flags.append("{}<->{}".format(k, v))
        for k, v in placed_map.items():
            flags.append("{}->{}".format(k, v))

        return flags


class Puzzle(object):
    def __init__(self, snd_blocks, draggable_blocks):
        self.snd_blocks = snd_blocks
        self.draggable_blocks = draggable_blocks

    def make_blockgroups(self):
        total_count = len(self.snd_blocks) + len(self.draggable_blocks)
        rows = int(math.ceil(total_count / 2))
        cols = 2
        startrow = 0

        block_queue = [(SelectableAndDraggableBlock, name) for name in self.snd_blocks]
        block_queue.extend([(DraggableBlock, name) for name in self.draggable_blocks])

        draggable_blocks = pygame.sprite.Group()
        snd_blocks = pygame.sprite.Group()

        for x in range(0, cols):
            for y in range(startrow, rows):
                cls, name = block_queue.pop()
                block = cls(x * 100 + 20, y * 100 + 20, name)
                draggable_blocks.add(block)
                if isinstance(block, SelectableAndDraggableBlock):
                    snd_blocks.add(block)

        # for x in range(0, 2):
        #     for y in range(0, 2):
        #         block = DraggableBlock(x * 100 + 20, y * 100 + 20, "draggable{}{}".format(x, y))
        #         draggable_blocks.add(block)
        #
        # for x in range(0, 2):
        #     for y in range(2, 4):
        #         block = SelectableAndDraggableBlock(x * 100 + 20, y * 100 + 20, "snd{}{}".format(x, y))
        #         snd_blocks.add(block)
        #         draggable_blocks.add(block)

        return {
            "snd_blockgroup": snd_blocks,
            "draggable_blockgroup": draggable_blocks
        }
