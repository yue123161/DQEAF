from gym.envs.registration import register

# get samples for environment
from graduation.tools import interface

sha256 = interface.get_available_sha256()
# create a holdout set
from sklearn.model_selection import train_test_split
import numpy as np

np.random.seed(123)
sha256_train, sha256_holdout = train_test_split(sha256, test_size=200)

MAXTURNS = 100

register(
    id='malware-v0',
    entry_point='graduation.envs:MalwareEnv',
    kwargs={'random_sample': True, 'maxturns': MAXTURNS, 'sha256list': sha256_train}
)

register(
    id='malware-test-v0',
    entry_point='graduation.envs:MalwareEnv',
    kwargs={'random_sample': False, 'maxturns': MAXTURNS, 'sha256list': sha256_holdout}
)

register(
    id='malware-score-v0',
    entry_point='graduation.envs:MalwareScoreEnv',
    kwargs={'random_sample': True, 'maxturns': MAXTURNS, 'sha256list': sha256_train}
)

register(
    id='malware-score-test-v0',
    entry_point='graduation.envs:MalwareScoreEnv',
    kwargs={'random_sample': False, 'maxturns': MAXTURNS, 'sha256list': sha256_holdout}
)