class Points_1D:
    def __init__(self, points):
        self._points = points
    
    def __len__(self):
        max_pt = max(self._points)
        min_pt = min(self._points)
        return max_pt - min_pt

if __name__ == '__main__':
    point_set = Points_1D((5, 8, 9, -5, -2, 18))
    print(len(point_set))
