class Node
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

def bfs(node)
  queue = []
  queue.push(node)

  while(queue.size != 0)
    node = queue.shift
    p node.val

    childrem = [ node.left, node.right ].compact

    childrem.each do |child|
      queue.push(child)
    end
  end
end

root = Node.new(3)

root_l = Node.new(9)
root_r = Node.new(20)
root.left = root_l
root.right = root_r

child__root_l__l = Node.new(33)
child__root_l__r = Node.new(25)
child__root_r__l = Node.new(15)
child__root_r__r = Node.new(7)

root_l.left = child__root_l__l #33
root_l.right = child__root_l__r #25
root_r.left = child__root_r__l #15
root_r.right = child__root_r__r #7


bfs(root)
