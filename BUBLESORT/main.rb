def buble_sort array
  array unless array.size > 1

  loop do
    flag = false

    (array.size - 1).times do |i|
      if array[i] > array[i+1]
        array[i], array[i+1] = array[i+1], array[i]
        flag = true
      end
    end
    break if not flag
  end
  array
end

array = [15, 26, 25, 4, 458, 3]
p buble_sort(array)
