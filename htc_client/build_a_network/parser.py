from build_a_network.entity import SelectableAndDraggableBlock, DraggableBlock


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
                # elif isinstance(list(blockgroup)[0])

        self.blockgroup_list = None
        return self

    def parse(self):
        self._populate()
        connect_map = {}
        for connect in self.connected:
            if connect.joined_to:
                connect_map[connect.name] = connect.joined_to.name
        tw = 2

