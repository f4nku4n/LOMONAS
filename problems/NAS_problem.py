class Problem:
    def __init__(self, maxEvals, name, dataset, **kwargs):
        """
        # Hyper-parameters:\n
        - *maxEvals* -> the maximum number of evaluated architecture.
        - *name* -> the name of used benchmark (or problem's name). E.g., MacroNAS, NAS-Bench-101, NAS-Bench-201, NAS-Bench-301.
        - *dataset* -> the dataset is used to train and evaluate architectures. E.g., CIFAR-10; CIFAR-100; ImageNet16-120
        - *objective_0* -> the first objective which we want to minimize. This objective usually is an efficiency metric.
        - *objective_1* -> the second objective which we want to minimize. This objective usually is the architecture's error.
        """
        self.maxEvals = maxEvals
        self.name = name
        self.dataset = dataset

        self.objective_0 = None
        self.objective_1 = None

    def reset(self):
        self._reset()

    def set_up(self):
        """
        - Set up necessary things.
        """
        self._set_up()
        if (self.objective_0 is None) or (self.objective_1 is None):
            raise ValueError('The optimization objectives have not been set up.')

    def sample_a_compact_architecture(self):
        """
        Sample a compact architecture in the search space.
        """
        return self._get_a_compact_architecture()

    def get_efficiency_metric(self, arch, **kwargs):
        """
        Get efficiency metric which be wanted to minimize, e.g., nFLOPs, nParams, MMACs, etc.
        """
        return self._get_efficiency_metric(arch, **kwargs)

    def get_val_performance_metric(self, arch, **kwargs):
        """
        Get performance metric which be wanted to minimize, e.g., accuracy, error, etc.
        """
        return self._get_val_performance_metric(arch, **kwargs)

    def isValid(self, arch):
        """
        - Checking if the architecture is valid or not.\n
        - NAS-Bench-101 doesn't provide information of all architecture in the search space. Therefore, when doing experiments on this benchmark, we need to check if the architecture is valid or not.\n
        """
        return self._isValid(arch)

    def calculate_IGD(self, approximation_front):
        return self._calculate_IGD(approximation_front)

    def _set_up(self):
        pass

    def _reset(self):
        pass

    def _get_a_compact_architecture(self):
        raise NotImplementedError

    def _get_efficiency_metric(self, arch, **kwargs):
        raise NotImplementedError

    def _get_val_performance_metric(self, arch, **kwargs):
        raise NotImplementedError

    def _isValid(self, arch):
        raise NotImplementedError

    def _calculate_IGD(self, approximation_front):
        raise NotImplementedError
