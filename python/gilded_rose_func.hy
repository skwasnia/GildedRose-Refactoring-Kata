(defn inc-quality-n [item n]
    (setv (. item quality)
        (min
            50
            (+ (. item quality) n)
        )
    )
)

(defn inc-quality [item]
    (inc-quality-n item 1)
)

(defn dec-quality [item]
    (when (> (. item quality) 0)
        (setv (. item quality) (- (. item quality) 1))
    )
)

(defn dec-sell-in [item]
    (setv (. item sell_in) (- (. item sell_in) 1))
)

(defn dec-quality-when-sell-in [item]
    (when (< (. item sell_in) 0)
        (dec-quality item)
    )
)

(defn inc-quality-when-sell-in [item]
    (when (< (. item sell_in) 0)
        (inc-quality item)
    )
)

(defn decrease-normal [item]
    (dec-quality item)
    (dec-sell-in item)
    (dec-quality-when-sell-in item)
)

(defn decrease-aged-brie [item]
    (inc-quality item)
    (dec-sell-in item)
    (inc-quality-when-sell-in item)
)

(defn backstage-increase [sell-in]
    (cond
        (<= sell-in 0) 0
        (<= sell-in 5) 3
        (<= sell-in 10) 2
        True 1
    )
)

(defn decrease-backstage-pass [item]
    (let [inc (backstage-increase (. item sell_in))]
        (inc-quality-n item inc)
    )

    (dec-sell-in item)

    ;; after the concert (use updated sell_in!)
    (when (< (. item sell_in) 0)
        (setv (. item quality) 0)
    )
)

(defn decrease-sulfuras [item]) ; Sulfuras does not change

(setv behavior-by-name
    {
        "Aged Brie" decrease-aged-brie
        "Sulfuras, Hand of Ragnaros" decrease-sulfuras
        "Backstage passes to a TAFKAL80ETC concert" decrease-backstage-pass
    }
)

; * In Lisp (and Hy), a list means "call the first thing with the rest as
;   arguments."
(defn apply-behavior [item]
    (let [behavior (.get behavior-by-name (. item name) decrease-normal)]
        (behavior item)
    )
)

(defn update-quality [items]
    (for [item items]
        (apply-behavior item)
    )
)
