import { expect } from "chai";
import { createQueue } from "kue";
import createPushNotificationsJobs from "./8-job";

describe('create job function js tests', () => {
  const queue = createQueue();

  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw error if jobs not array', () => {
    expect(() => createPushNotificationsJobs('!array', queue))
    .to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs based on each object on array', () => {
    const jobs = [
      { phoneNumber: '12345678', message: 'msg_test_1' },
      { phoneNumber: '09876543', message: 'msg_test_2' }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal({phoneNumber: '12345678', message: 'msg_test_1'});
    expect(queue.testMode.jobs[1].data).to.deep.equal({phoneNumber: '09876543', message: 'msg_test_2'});
  });
})
