class NormalizationModel:
    def __init__(self, items):
        """
        items = [
            {"tag": str, "count": int, "is_selected": False, "is_norm": False, "norm_value": None},
            ...
        ]
        """
        self.items = items
        self.current_norm = None

        # Filterstrings für die drei Fenster
        self.filter_left = ""
        self.filter_norm = ""
        self.filter_details = ""

        # Sortierung für linkes Fenster
        self.sort_left_by = 1  # Spalte 1 (TAG-Wert) standardmäßig
        self.sort_left_order = 0  # 0=aufsteigend, 1=absteigend

        # Sortierung für mittleres Fenster (Normwerte)
        self.sort_norm_by = 0  # Spalte 0 (Normwert) standardmäßig
        self.sort_norm_order = 0  # 0=aufsteigend, 1=absteigend

        # Sortierung für rechtes Fenster (Details)
        self.sort_details_by = 0  # Spalte 0 (TAG-Wert) standardmäßig
        self.sort_details_order = 0  # 0=aufsteigend, 1=absteigend

    # ---------------------------------------------------------
    # Hilfsfunktionen
    # ---------------------------------------------------------
    def _matches_filter(self, text, filter_string):
        if not filter_string:
            return True
        return filter_string.lower() in text.lower()

    def _get_item(self, tag):
        for item in self.items:
            if item["tag"] == tag:
                return item
        return None

    # ---------------------------------------------------------
    # Linkes Fenster
    # ---------------------------------------------------------
    def get_left_items(self):
        """Alle TAG-Werte ohne Normwert, gefiltert."""
        return [
            item for item in self.items
            if item["norm_value"] is None
            and self._matches_filter(item["tag"], self.filter_left)
        ]

    def set_norm_value(self, tag):
        """Macht einen TAG-Wert zum Normwert."""
        item = self._get_item(tag)
        if not item:
            return

        item["is_norm"] = True
        item["norm_value"] = tag
        self.current_norm = tag

    def assign_to_current_norm(self, tags):
        """Weist mehrere TAG-Werte dem aktuellen Normwert zu."""
        if not self.current_norm:
            return

        for tag in tags:
            item = self._get_item(tag)
            if item:
                item["norm_value"] = self.current_norm
                item["is_selected"] = False

    def assign_single(self, tag):
        """Doppelklick im linken Fenster."""
        if not self.current_norm:
            return
        item = self._get_item(tag)
        if item:
            item["norm_value"] = self.current_norm

    # ---------------------------------------------------------
    # Mittleres Fenster
    # ---------------------------------------------------------
    def get_norm_values(self):
        norms = {}

        for item in self.items:
            nv = item["norm_value"]
            if nv is None:
                continue

            if nv not in norms:
                norms[nv] = {"count_items": 0, "sum_counts": 0}

            norms[nv]["count_items"] += 1
            norms[nv]["sum_counts"] += item["count"]

        # gefilterte Liste
        result = [
            {"norm": nv, **data}
            for nv, data in norms.items()
            if self._matches_filter(nv, self.filter_norm)
        ]

        # current_norm immer anzeigen
        cn = self.current_norm
        if cn and cn in norms:
            if not any(entry["norm"] == cn for entry in result):
                data = norms[cn]
                result.append({"norm": cn, **data})

        return result

    def select_norm(self, norm_value):
        """Setzt den aktuellen Normwert."""
        self.current_norm = norm_value

    def rename_norm_value(self, old_norm: str, new_norm: str):
        """
        Benennt einen Normwert um, ohne die ursprünglichen TAG-Werte zu verändern.

        - Alle Items mit norm_value == old_norm bekommen norm_value = new_norm.
        - Falls es ein Item mit tag == new_norm gibt, wird dieses ebenfalls
        dem neuen Normwert zugeordnet (norm_value = new_norm).
        """

        # 1. Alle bisherigen Zuordnungen von old_norm auf new_norm umbiegen
        for item in self.items:
            if item["norm_value"] == old_norm:
                item["norm_value"] = new_norm

        # 2. Falls es einen TAG-Wert gibt, der exakt dem neuen Normwert entspricht,
        #    diesen ebenfalls dem Normwert zuordnen
        for item in self.items:
            if item["tag"] == new_norm:
                item["norm_value"] = new_norm

        # 3. current_norm aktualisieren
        if self.current_norm == old_norm:
            self.current_norm = new_norm

    def delete_norm_value(self, norm_value):
        """Normwert löschen, alle Detailwerte zurück nach links."""
        for item in self.items:
            if item["norm_value"] == norm_value:
                item["norm_value"] = None
            if item["tag"] == norm_value:
                item["is_norm"] = False
        if self.current_norm == norm_value:
            self.current_norm = None

    # ---------------------------------------------------------
    # Rechtes Fenster
    # ---------------------------------------------------------
    def get_details_for_current_norm(self):
        """Alle Detailwerte des aktuellen Normwerts."""
        if not self.current_norm:
            return []

        return [
            item for item in self.items
            if item["norm_value"] == self.current_norm
            and self._matches_filter(item["tag"], self.filter_details)
        ]

    def remove_detail(self, tag):
        """Detailwert entfernen → zurück nach links."""
        item = self._get_item(tag)
        if item:
            item["norm_value"] = None
            item["is_selected"] = False

    def delete_all_norms(self):
        """Löscht alle Normwerte und setzt alle TAG-Werte zurück."""
        for item in self.items:
            item["norm_value"] = None
            item["is_norm"] = False
            item["is_selected"] = False

        self.current_norm = None

    # ---------------------------------------------------------
    # Step 3 – Statistiken und Ersetzungsliste
    # ---------------------------------------------------------
    def count_original_values(self):
        """Anzahl unterschiedlicher Original-TAG-Werte."""
        return len(self.items)

    def count_norm_values(self):
        """Anzahl unterschiedlicher Normwerte."""
        return len(self.get_norm_values())

    def count_replacements(self):
        """
        Anzahl der Werte, die tatsächlich ersetzt werden.
        Das sind alle Items, bei denen eine Ersetzung stattfindet
        (tag != norm_value).
        """
        return sum(
            1
            for item in self.items
            if item["norm_value"] is not None and item["norm_value"] != item["tag"]
        )

    def count_total_occurrences(self):
        """Gesamtzahl aller Vorkommen (Summe der counts)."""
        return sum(item["count"] for item in self.items)

    def get_replacement_list(self):
        """
        Liefert eine Liste von (alt, neu, count) für alle Items,
        bei denen eine Ersetzung stattfindet.
        """
        replacements = []
        for item in self.items:
            old = item["tag"]
            new = item["norm_value"]
            count = item["count"]

            if new is not None and new != old:
                replacements.append((old, new, count))

        return replacements        