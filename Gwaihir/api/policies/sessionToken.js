module.exports = function (req, res, next) {
  if (req.session.token) {
    return next();
  }
  return res.redirect('/');
}