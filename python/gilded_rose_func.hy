; * Item -> Item (via mutation): Mutation is just an implicit state monad.
(defn inc-quality-n [item n 1]
    (setv (. item quality)
        (min
            50
            (+ (. item quality) n)
        )
    )
)

(defn dec-quality [item]
    (when (> (. item quality) 0)
        (setv (. item quality) (- (. item quality) 1))
    )
)

(defn dec-sell-in [item]
    (setv (. item sell_in) (- (. item sell_in) 1))
)

; * Build types with AND: item has name AND sell_in AND quality.
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

; * Sequential composition: combine small functions to build bigger ones -
;   monoidal composition of transformations - which becomes monadic sequencing
;   when effects are involved.
(defn decrease-normal [item]
    (dec-quality item)
    (dec-sell-in item)
    (dec-quality-when-sell-in item)
)

; * "Types are not classes": We separated what the data is from how it changes.
(defn decrease-aged-brie [item]
    (inc-quality item)
    (dec-sell-in item)
    (inc-quality-when-sell-in item)
)

;-------------------------------------------------------------------------------
; Bakcstage passes behavior
;-------------------------------------------------------------------------------
(defn backstage-increase [sell-in]
    (cond
        (<= sell-in 0) 0
        (<= sell-in 5) 3
        (<= sell-in 10) 2
        True 1
    )
)

(defn inc-backstage-quality-before-concert [item]
    (inc-quality
        item
        (backstage-increase (. item sell_in))
    )
)

(defn zero-quality-when-after-concert [item]
    (when (< (. item sell_in) 0)
        (setv (. item quality) 0)
    )
)

(defn decrease-backstage-pass [item]
    (inc-backstage-quality-before-concert item)
    (dec-sell-in item)
    (zero-quality-when-after-concert item)
)

(defn decrease-sulfuras [item]) ; Sulfuras does not change

(defn make-apply-behavior [behavior-by-name]
    (fn [item](
            (.get behavior-by-name (. item name) decrease-normal)
            item
        )
    )
)

(setv apply-behavior
    ; * Build types with OR: item behavior chosen based on name
    (make-apply-behavior
        {
            "Aged Brie" decrease-aged-brie
            "Sulfuras, Hand of Ragnaros" decrease-sulfuras
            "Backstage passes to a TAFKAL80ETC concert" decrease-backstage-pass
        }
    )
)

; * Tunnel of transformation - Lists support map/sequence - monadic behavior
(defn update-quality [items]
    (for [item items]
        (apply-behavior item)
    )
)
