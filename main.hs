type Adj a = [a]
type Context a = (Adj a, a, Adj a)
data Graph a = Empty | Context a :& Graph a

data Labeled a = Labeled (a -> String) (Graph a)
data Named a = Named String (Labeled a)

-- show the graph in dot format
instance Show (Labeled a) where
  show (Labeled label Empty) = ""
  show (Labeled label (c :& g)) = (showContext c) ++ (show (Labeled label g)) where
    showContext ([], n, []) = "\"" ++ label n ++ "\";\n"
    showContext (i, n, o) = concatMap (showArc n) o ++ concatMap (flip showArc n) i where
      showArc from to = "\"" ++ (label from) ++ "\" -> \"" ++ (label to) ++ "\";\n"
instance Show (Named a) where
  show (Named name labeled) = "digraph \"" ++ name ++ "\" {\n" ++ (show labeled) ++ "}\n"


gmap :: (Context a -> Context a) -> Graph a -> Graph a
gmap f Empty = Empty
gmap f (c :& g) = (f c) :& (gmap f g)

gnodes :: Graph a -> [a]
gnodes Empty = []
gnodes ((_, n, _) :& g) = n:gnodes g

fromnodes :: [a] -> Graph a
fromnodes [] = Empty
fromnodes (n:nodes) = ([], n, []) :& (fromnodes nodes)

-- Model assumptions:
-- 1. We work in 12-tone equal temperament.
-- 2. Tones are equivalent modulo octaves.

addquints :: (Context Int) -> (Context Int)
addquints (i, n, o) = (i, n, ((n + 7) `mod` 12):o)
mygraph = gmap addquints $ fromnodes [0..11]

notes = [ "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B" ]
label n = notes !! n
main = do print (Named "harmony" (Labeled label (mygraph)))
